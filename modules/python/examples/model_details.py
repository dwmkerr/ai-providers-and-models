#!/usr/bin/env python3
"""
Example script to display the AI providers and models.
This script loads the bundled models.yaml file and prints a summary.
"""

from ai_providers_and_models import providers


def main():
    # Show OpenAI models
    openai_provider = providers["openai"]
    print(f"\033[94m\033[1m{openai_provider.name} Models\033[0m")

    for model_id, model in openai_provider.models.items():
        status = "✓" if model.validated else " "
        default_version = next((v for v in model.versions if v.isDefault), None) if model.versions else None
        version_info = f"default: {default_version.id}" if default_version else "no version info"

        print(f"[{status}] {model_id} ({version_info})")
        print(f"    Name: {model.name}")
        print(f"    Status: {model.status}")
        print(f"    Knowledge cutoff: {model.knowledgeCutoff}")
        print(f"    Pricing: ${model.pricing.input_per_million}/M input, ${model.pricing.output_per_million}/M output")
        print()


if __name__ == "__main__":
    main()
