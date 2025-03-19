"""
ai_providers_and_models

This package provides type-safe access to a collection of AI providers and
their models, which are defined in a YAML configuration file. The
configuration is automatically loaded at package initialisation, making the
providers available via the `providers` variable.

Usage:
    from ai_providers_and_models import providers
    for provider_id, provider in providers.items():
        print(provider.name)

Dependencies:
    - PyYAML: For parsing the YAML file.
    - Pydantic: For type validation and data modeling.

Ensure that the YAML file (models.yaml) is included as package data.
"""
from .providers_file import load_providers_file

# Load the models yaml. Try Python 3.9 files first.
try:
    from importlib.resources import files
    data_path = (
        files("ai_providers_and_models.data").joinpath("models.yaml")
    )
    data = data_path.read_text(encoding="utf-8")
# ...fall back to read_text.
except ImportError:
    from importlib.resources import read_text
    data = read_text("ai_providers_and_models.data", "models.yaml")
except Exception as e:
    # Optionally, handle or log the error if the YAML fails to load.
    raise RuntimeError("Failed to load providers from models.yaml") from e

# Now read the providers file data.
providers_file = load_providers_file(data)
providers = providers_file.providers
