import yaml
from .models import ProvidersFile


def load_providers_file(data: str) -> ProvidersFile:
    parsed = yaml.safe_load(data)
    return ProvidersFile(**parsed)
