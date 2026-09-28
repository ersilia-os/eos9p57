# imports
import csv
import os
import sys
from typing import List

import numpy as np
from crem.crem import grow_mol
from rdkit import DataStructs
from rdkit.Chem import MolFromSmiles, MolToSmiles, rdMolDescriptors
from sklearn.cluster import MiniBatchKMeans
from sklearn.metrics import pairwise_distances_argmin_min

from ersilia_pack_utils.core import read_smiles

# parse arguments
input_file = sys.argv[1]
output_file = sys.argv[2]

# current file directory
root = os.path.dirname(os.path.abspath(__file__))

# Path to ChEMBL dataset with fragments of SC score 2 (same DB eos4q1a uses)
database_dir = os.path.abspath(os.path.join(root, "..", "..", "checkpoints"))
database_path = os.path.join(database_dir, "replacements02_sc2.db")


def generate_fingerprint(mol, nbits, radius=3) -> np.ndarray:
    """
    Return Morgan Fingerprint for a molecule as a fixed shape Numpy array.
    """
    arr = np.zeros((1, nbits), dtype=np.int32)
    fp = rdMolDescriptors.GetHashedMorganFingerprint(mol, radius=radius, nBits=nbits)
    DataStructs.ConvertToNumpyArray(fp, arr)
    return arr.reshape(1, nbits)


def sample_molecules(smiles: List[str]) -> List[str]:
    """
    Samples generated molecules into 100 clusters by fitting a K-Means clustering model
    and returns the molecules closest to each cluster centre.
    """
    features = 2048
    max_sampled = 2000
    sampled_smiles: List[str] = []
    num_smiles = len(smiles)

    if num_smiles > max_sampled:
        smiles = np.random.choice(smiles, max_sampled, replace=False).tolist()

    mol_fps = np.zeros((len(smiles), features))
    for i, smi in enumerate(smiles):
        mol_fps[i] = generate_fingerprint(MolFromSmiles(smi), features)

    mbkm_estimator = MiniBatchKMeans(n_clusters=100)
    mbkm_estimator.fit(mol_fps)
    closest, _ = pairwise_distances_argmin_min(
        mbkm_estimator.cluster_centers_, mol_fps, metric="euclidean"
    )
    for idx in closest:
        sampled_smiles.append(smiles[idx])
    return sampled_smiles


def my_model(smiles_list: List[str]) -> List[List[str]]:
    output_smiles = []
    for smi in smiles_list:
        mol = MolFromSmiles(smi)
        try:
            growth_result = list(grow_mol(mol=mol, db_name=database_path, ncores=2))
        except Exception:
            growth_result = []  # Nothing generated

        # Dedup by canonical SMILES, not the raw generator-yielded string: CReM can
        # yield two different SMILES strings for the same canonical molecule.
        seen = set()
        generated_smiles = []
        for s in growth_result:
            m = MolFromSmiles(s)
            key = MolToSmiles(m) if m is not None else s
            if key in seen:
                continue
            seen.add(key)
            generated_smiles.append(s)

        num_generated_smiles = len(generated_smiles)

        if num_generated_smiles > 100:
            generated_smiles = sample_molecules(smiles=generated_smiles)
        elif num_generated_smiles < 100:
            generated_smiles = generated_smiles + [""] * (100 - num_generated_smiles)

        output_smiles.append(generated_smiles)

    return output_smiles


# read SMILES from .csv file, assuming one column with header
_, smiles_list = read_smiles(input_file)

# run model
outputs = my_model(smiles_list)

# check input and output have the same length
assert len(smiles_list) == len(outputs)

# write output in a .csv file
header = [f"smi_{str(i).zfill(2)}" for i in range(100)]
with open(output_file, "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(header)
    for row in outputs:
        writer.writerow(row)
