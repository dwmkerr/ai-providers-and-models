# ai_providers_and_models

The Python API for [`ai-providers-and-models`](https://github.com/dwmkerr/ai-providers-and-models).

## Setup

Install dev dependencies and link the `models.yaml` into the development environment:

```bash
make init
```

## Deploy

Deploy to [TestPyPi](https://test.pypi.org) first then test the examples:

```bash
# Note: safer to publish as an RC while testing...
# Edit pyproject.toml
# version = "0.1.0rc1"
make build
twine upload --repository testpypi dist/*

# Create and activate a new venv.
python3 -m venv test_apam
source test_apam/bin/activate

# Upgrade pip and install from TestPypi. Note that dependencies like PyYAML
# are installed from the main PyPi repository. Note we also instal prerelease.
pip install --upgrade pip
pip install --upgrade --pre --index-url https://test.pypi.org/simple/ --extra-index-url https://pypi.org/simple  ai_providers_and_models

# Show the versions.
pip index versions --pre --index-url https://test.pypi.org/simple/ ai_providers_and_models

# Run the examples.
for example in ./examples/*; do
    [[ -e "${example}" ]] && python3 "${example}"
done

# Deactivate and delete the venv
deactivate
```

Then deploy to PyPi:

```bash
make build
twine upload dist/*
```
