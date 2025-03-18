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
from .models import load_providers_yaml

# Load the providers.
try:
    providers = load_providers_yaml().providers
except Exception as e:
    # Optionally, handle or log the error if the YAML fails to load.
    raise RuntimeError("Failed to load providers from models.yaml") from e
