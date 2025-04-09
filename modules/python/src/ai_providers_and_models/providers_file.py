import yaml
from .models import ProvidersFile


def load_providers_file(data: str) -> ProvidersFile:
    # Use yaml.SafeLoader to prevent automatic date parsing
    class SafeLoaderNoDateParsing(yaml.SafeLoader):
        @classmethod
        def remove_implicit_resolver(cls, tag_to_remove):
            """Remove implicit resolvers for a particular tag"""
            if not 'yaml_implicit_resolvers' in cls.__dict__:
                cls.yaml_implicit_resolvers = cls.yaml_implicit_resolvers.copy()
            for first_letter, mappings in cls.yaml_implicit_resolvers.items():
                cls.yaml_implicit_resolvers[first_letter] = [(tag, regexp)
                                                           for tag, regexp in mappings
                                                           if tag != tag_to_remove]

    # Remove the resolver for dates
    SafeLoaderNoDateParsing.remove_implicit_resolver('tag:yaml.org,2002:timestamp')
    
    parsed = yaml.load(data, SafeLoaderNoDateParsing)
    return ProvidersFile(**parsed)
