# CReM Growth-Based Structure Generation

Generates new analogues of an input molecule by attaching a small fragment (1-2 heavy atoms) from a curated ChEMBL fragment database to an available hydrogen position. Every atom and bond of the original structure is preserved intact. Uses the GROW mode of the CReM framework; up to 100 diverse analogues are returned per input via K-Means clustering. Cannot create new ring systems, so ring diversity is limited by the fragment database.

This model was incorporated on 2026-09-28.Last packaged on 2026-09-28.

## Information
### Identifiers
- **Ersilia Identifier:** `eos9p57`
- **Slug:** `crem-grow`

### Domain
- **Task:** `Sampling`
- **Subtask:** `Generation`
- **Biomedical Area:** `Any`
- **Target Organism:** `Any`
- **Tags:** `Compound generation`

### Input
- **Input:** `Compound`
- **Input Dimension:** `1`

### Output
- **Output Dimension:** `100`
- **Output Consistency:** `Variable`
- **Interpretation:** Up to 100 new molecules per input, each retaining the original structure with new fragments added at hydrogen positions.

Below are the **Output Columns** of the model:
| Name | Type | Direction | Description |
|------|------|-----------|-------------|
| smi_00 | string |  | Generated molecule index 0 using the CReM GROW molecular generator |
| smi_01 | string |  | Generated molecule index 1 using the CReM GROW molecular generator |
| smi_02 | string |  | Generated molecule index 2 using the CReM GROW molecular generator |
| smi_03 | string |  | Generated molecule index 3 using the CReM GROW molecular generator |
| smi_04 | string |  | Generated molecule index 4 using the CReM GROW molecular generator |
| smi_05 | string |  | Generated molecule index 5 using the CReM GROW molecular generator |
| smi_06 | string |  | Generated molecule index 6 using the CReM GROW molecular generator |
| smi_07 | string |  | Generated molecule index 7 using the CReM GROW molecular generator |
| smi_08 | string |  | Generated molecule index 8 using the CReM GROW molecular generator |
| smi_09 | string |  | Generated molecule index 9 using the CReM GROW molecular generator |

_10 of 100 columns are shown_
### Source and Deployment
- **Source:** `Local`
- **Source Type:** `External`
- **DockerHub**: [https://hub.docker.com/r/ersiliaos/eos9p57](https://hub.docker.com/r/ersiliaos/eos9p57)
- **Docker Architecture:** `AMD64`, `ARM64`
- **S3 Storage**: [https://ersilia-models-zipped.s3.eu-central-1.amazonaws.com/eos9p57.zip](https://ersilia-models-zipped.s3.eu-central-1.amazonaws.com/eos9p57.zip)

### Resource Consumption
- **Model Size (Mb):** `688`
- **Environment Size (Mb):** `661`
- **Image Size (Mb):** `2006.06`

**Computational Performance (seconds):**
- 10 inputs: `29.88`
- 100 inputs: `150.74`
- 10000 inputs: `-1`

### References
- **Source Code**: [https://github.com/DrrDom/crem](https://github.com/DrrDom/crem)
- **Publication**: [https://doi.org/10.1186/s13321-020-00431-w](https://doi.org/10.1186/s13321-020-00431-w)
- **Publication Type:** `Peer reviewed`
- **Publication Year:** `2020`
- **Ersilia Contributor:** [arnaucoma24](https://github.com/arnaucoma24)

### License
This package is licensed under a [GPL-3.0](https://github.com/ersilia-os/ersilia/blob/master/LICENSE) license. The model contained within this package is licensed under a [BSD-3-Clause](LICENSE) license.

**Notice**: Ersilia grants access to models _as is_, directly from the original authors, please refer to the original code repository and/or publication if you use the model in your research.


## Use
To use this model locally, you need to have the [Ersilia CLI](https://github.com/ersilia-os/ersilia) installed.
The model can be **fetched** using the following command:
```bash
# fetch model from the Ersilia Model Hub
ersilia fetch eos9p57
```
Then, you can **serve**, **run** and **close** the model as follows:
```bash
# serve the model
ersilia serve eos9p57
# generate an example file
ersilia example -n 3 -f my_input.csv
# run the model
ersilia run -i my_input.csv -o my_output.csv
# close the model
ersilia close
```

## About Ersilia
The [Ersilia Open Source Initiative](https://ersilia.io) is a tech non-profit organization fueling sustainable research in the Global South.
Please [cite](https://github.com/ersilia-os/ersilia/blob/master/CITATION.cff) the Ersilia Model Hub if you've found this model to be useful. Always [let us know](https://github.com/ersilia-os/ersilia/issues) if you experience any issues while trying to run it.
If you want to contribute to our mission, consider [donating](https://www.ersilia.io/donate) to Ersilia!
