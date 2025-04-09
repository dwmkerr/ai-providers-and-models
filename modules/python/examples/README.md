# Examples

This directory contains example scripts that demonstrate how to use the `ai_providers_and_models` package.

## Available Examples

### Model Details

Display detailed information about OpenAI models, including their validation status, versions, and pricing.

```bash
python examples/model_details.py
```

Example output:
```
OpenAI Models
[✓] gpt-4o (default: gpt-4o-2024-08-06)
    Name: GPT-4o
    Status: general-availability
    Knowledge cutoff: October 2023
    Pricing: $2.5/M input, $10.0/M output

[✓] gpt-4 (default: gpt-4-0613)
    Name: GPT-4
    Status: general-availability
    Knowledge cutoff: December 2023
    Pricing: $30.0/M input, $60.0/M output
```

### List Providers

List all providers available in the configuration.

```bash
python examples/list_providers.py
```

Example output:
```
OpenAI
id: openai
models: 6

Gemini
id: gemini
models: 3
```

### List Models

List all models from all providers.

```bash
python examples/list_models.py
```

Example output:
```
OpenAI
  GPT-4o: Fast, intelligent, flexible GPT model
  GPT-4.5: Enhanced GPT model with improved reasoning and conversational abilities
  o3-mini: Fast, flexible, intelligent reasoning model

Gemini
  Gemini 2.0 Flash: Our newest multimodal model, with next generation features and improved capabilities
  Gemini 2.0 Flash-Lite: A Gemini 2.0 Flash model optimized for cost efficiency and low latency
```

## Running the Examples

To run these examples:

1. Make sure you have the package installed:
   ```bash
   # From the modules/python directory
   pip install -e .
   ```

2. Run any example script:
   ```bash
   python examples/model_details.py
   ```

## Integration with Other Tools

These examples can be useful for:

1. Quickly checking model availability and configuration
2. Comparing pricing across different models
3. Identifying which models have been validated
4. Understanding model version information