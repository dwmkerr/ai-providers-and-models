#!/usr/bin/env python3
"""
Example script to display the AI providers and models.
This script loads the bundled models.yaml file and prints a summary.
"""

from ai_providers_and_models import providers


def main():
    model = providers["gemini"].models["models/gemini-2.0-flash"]
    print(model.pricing.input_per_million)
    print(model.modalities)


if __name__ == "__main__":
    main()
