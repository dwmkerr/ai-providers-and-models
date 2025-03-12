# ai-providers-and-models

Work in progress. Regularly updated list of AI providers and models, available for mulitple languages and platforms.

## Usage

The [`models.yaml`](./models.yaml) file contains details of available OpenAI models and their capabilities.

A short snippet is below - the `models.yaml` file is more complete.

```yaml
version: 0.1.0
updated: 2025-03-12
source: https://github.com/dwmkerr/ai-providers-and-models
providers:
  - name: openai
    docs: https://platform.openai.com/docs/models
    models:
      - id: gpt-4
        verified: false
        name: GPT-4
        docs: https://platform.openai.com/docs/models/gpt-4
        description: A large multimodal model accepting text and image inputs, known for reliability and creativity.
        short_description: Reliable and creative, accepts text and images.
        modalities:
          text: true
          image: true
          audio: false
        endpoints:
          chat_completions: true
          realtime: false
          # etc,,,
        price:
          per_million_input_tokens: 30000
          per_million_output_tokens: 60000
        context_window_tokens: 8192
        max_output_tokens: 2048

      - id: gpt-4-32k
        # etc...
```
