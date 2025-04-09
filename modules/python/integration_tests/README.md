# Integration Tests

This directory contains integration tests for the `ai_providers_and_models` package that verify models work correctly with their respective APIs.

## Provider-Specific Tests

These tests verify that models listed in the configuration can be successfully initialized and used with their respective provider SDKs.

### Requirements

- API key for the respective provider (set as environment variable)
- Provider's Python SDK package

### Usage

```bash
# Set your provider's API key
export PROVIDER_API_KEY=your_api_key_here

# Run from the modules/python directory
cd modules/python
python -m integration_tests.test_provider_models
```

Where `provider` is one of:
- `openai`
- `anthropic` 
- `google`

## OpenAI Tests

The OpenAI tests verify that models listed in the configuration can be successfully initialized and used with the OpenAI Python SDK.

### Requirements

- OpenAI API key (set as environment variable)
- `openai` Python package

### Usage

```bash
# Set your OpenAI API key
export OPENAI_API_KEY=your_api_key_here

# Run from the modules/python directory
cd modules/python
python -m integration_tests.test_openai_models
```

### What the Tests Do

1. Display a summary table of all configured OpenAI models
2. Test each model by sending a simple completion request
3. Report which models succeeded and which failed

### Example Output

```
OpenAI Models Integration Test
--------------------------------------------------------------------------------
Model ID             Name                Status          Validated   
--------------------------------------------------------------------------------
gpt-4o              GPT-4o              general-availa... ✓         
gpt-4.5-preview     GPT-4.5             preview          ✗         
o3-mini             o3-mini             preview          ✓         
o1                  o1                  general-availa... ✓         
gpt-4o-mini-2024-07-18 GPT-4o mini        preview          ✗         
gpt-4               GPT-4               general-availa... ✓         
--------------------------------------------------------------------------------

testing 6 OpenAI models:
testing gpt-4o (GPT-4o)...
✅ gpt-4o: success (1.23s): GPT-4o features include fast processing, high intelligence, flexibility, and support for both te...
testing gpt-4.5-preview (GPT-4.5)...
✅ gpt-4.5-preview: success (2.45s): GPT-4.5 offers enhanced reasoning abilities, improved factual accuracy, and superior conv...
testing o3-mini (o3-mini)...
✅ o3-mini: success (0.87s): O3-mini is a small reasoning model with high intelligence, low latency, and support for key deve...
testing o1 (o1)...
✅ o1: success (3.12s): The main features of the o1 model include high-intelligence reasoning with reinforcement learning...
testing gpt-4o-mini-2024-07-18 (GPT-4o mini)...
✅ gpt-4o-mini-2024-07-18: success (0.92s): GPT-4o mini is a fast, affordable small model for focused tasks with multimodal...
testing gpt-4 (GPT-4)...
✅ gpt-4: success (2.31s): GPT-4 is an older high-intelligence GPT model with strong reasoning capabilities.

results: 6/6 models tested successfully
```

## Future Improvements

- Add support for testing other providers (Gemini, Claude)
- Add support for testing specific capabilities (image input, structured output)
- Add support for updating the `validated` field in models.yaml based on test results