#!/usr/bin/env python3
"""
Example script to display the AI providers and models.
This script loads the bundled models.yaml file and prints a summary.
"""

from ai_providers_and_models import providers


def main():
    # Loop through each provider and display summary details.
    for provider in providers.values():
        # Print the provider's name in blue bold
        print(f"\033[94m\033[1m{provider.name}\033[0m")
        # Loop through all models for this provider.
        for model in provider.models.values():
            indent = "  "
            # Print the model name in green bold then a grey description.
            print(
                f"{indent}\033[92m\033[1m{model.name}\033[0m" +
                f"\033[90m: {model.description_short}\033[0m"
            )


if __name__ == "__main__":
    main()
