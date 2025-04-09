# Integration Tests

This directory contains integration tests that verify models can be successfully used with their respective provider APIs.

## How to Run

```bash
# Set your OpenAI API key
export OPENAI_API_KEY=your_api_key_here

# Run from the modules/python directory
cd modules/python
python -m integration_tests.test_openai_models
```

## What It Does

The integration tests:
1. Check that all configured models can be initialized
2. Send a simple completion request to each model
3. Report which models succeeded and which failed

## Future Improvements

- Add support for testing other providers (Gemini, Claude)
- Add support for testing specific capabilities (image input, structured output)
- Add support for updating the `validated` field in models.yaml based on test results