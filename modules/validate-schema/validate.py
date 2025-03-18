#!/usr/bin/env python
"""
validate.py: Validate a YAML file against a JSON Schema.

Usage:
    validate.py <yaml-file> <schema-file>
"""
import sys
from ruamel.yaml import YAML
import jsonschema
from jsonschema.exceptions import ValidationError


def load_yaml(file):
    """Load a YAML file, ensuring dates remain as strings."""
    yaml = YAML(typ='safe')
    yaml.constructor.yaml_constructors[
        'tag:yaml.org,2002:timestamp'
    ] = yaml.constructor.yaml_constructors['tag:yaml.org,2002:str']
    try:
        with open(file, encoding='utf-8') as f:
            return yaml.load(f)
    except Exception as exc:
        print(f"❌ Error parsing '{file}':\n{exc}")
        sys.exit(1)


def count_fields(models_list):
    """Count all individual fields in each model."""
    return sum(len(model.keys()) for model in models_list)


def validate(yaml_data, schema, yaml_file, schema_file):
    """Validate YAML data against a JSON schema and print a summary."""
    try:
        jsonschema.validate(instance=yaml_data, schema=schema, cls=jsonschema.Draft202012Validator)
        providers_dict = yaml_data.get("providers", {})
        total_providers = len(providers_dict)
        total_models = sum(
            len(p["models"]) for p in providers_dict.values()
        )
        total_fields = sum(
            count_fields(list(p["models"].values())) for p in providers_dict.values()
        )

        print("✅ Validation Passed!")
        print(f"   Providers: {total_providers} | Models: {total_models} "
              f"| Total fields checked: {total_fields}")
        print(f"   Version: {yaml_data.get('version', '-')}, "
              f"Updated: {yaml_data.get('updated', '-')}")
    except ValidationError as e:
        error_path = '.'.join(str(part) for part in e.absolute_path) or "<root>"
        schema_path = '.'.join(str(p) for p in e.absolute_schema_path) or "<schema root>"
        print("❌ YAML validation failed!")
        print(f"   Problem: {e.message}")
        print(f"   At YAML path: {error_path}")
        print(f"   Schema rule location: {schema_path}")
        sys.exit(1)


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print(f"Usage: {sys.argv[0]} <yaml-file> <schema-file>")
        sys.exit(1)

    yaml_file, schema_file = sys.argv[1], sys.argv[2]
    yaml_data = load_yaml(yaml_file)
    schema = load_yaml(schema_file)
    validate(yaml_data, schema, yaml_file, schema_file)
