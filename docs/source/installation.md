# Installation

## Install python package

### Using pip

Your ssh key must be present on <https://github.com/-/profile/keys>.

```bash
pip install git+ssh://git@github.com/laurent-attias/python_aimaira_odata.git
```

### Using pip in a virtual environment

```bash
git clone https://github.com/laurent-attias/python_aimaira_odata.git
cd python_aimaira_odata
python3 -m virtualenv .venv  # create a virtual environment
source .venv/bin/activate  # activate the virtual environment
pip install -e .  # install the package in editable mode
```

Note: in editable mode (`-e` option), the package is installed in a way that it is still possible to edit the source code and have the changes take effect immediately.

## Run the unitary tests

### Install the development dependencies

```bash
pip install -e ".[test]"
```

### Run the tests

Run the tests from the projet root directory using the `-s`:

```bash
pytest -sv
```

## Build the documentation

### Install the documentation dependencies

```bash
pip install -e ".[doc]"
```

### Build and serve the documentation locally

```bash
sphinx-autobuild docs/source/ docs/_build/html
```

Go to <http://localhost:8000> and see the changes in `docs/source/` directory take effect immediately.
