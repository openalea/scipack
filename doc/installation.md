# Installation

You must use conda environment : <https://docs.conda.io/en/latest/index.html>

## Users

### Create a new environment with scipack installed in there

```bash

mamba create -n scipack -c openalea3 -c conda-forge  openalea.scipack
mamba activate scipack
```

Install scipack in a existing environment

```bash
mamba install -c openalea3 -c conda-forge openalea.scipack
```

### (Optional) Test your installation

```bash
mamba install -c conda-forge pytest
git clone https://github.com/openalea/scipack.git
cd scipack/test; pytest
```

## Developers

### Install From source

```bash
# Install dependency with conda
mamba env create -n phm -f conda/environment.yml
mamba activate scipack

# Clone scipack and install
git clone https://github.com/openalea/scipack.git
cd scipack
pip install .

# (Optional) Test your installation
cd test; pytest
```
