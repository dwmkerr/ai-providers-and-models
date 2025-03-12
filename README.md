# ai-providers-and-models

Work in progress. Regularly updated list of AI providers and models, available for multiple languages and platforms.

I'm looking for help! Please do contribute if you think this would be useful!

Important:

- Pricing information is best effort from online documentation, be cautious using this data
- Any model with `validated: true` has been at least partly tested using [Terminal AI](https://github.com/dwmkerr/terminal-ai) and should work for chat and completion API calls
- This is very much early days work in progress, the schema and API will certainly change

:
<!-- vim-markdown-toc GFM -->

- [Usage](#usage)
- [NodeJS](#nodejs)
- [Status](#status)

<!-- vim-markdown-toc -->

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

## NodeJS

Usage:

```node
import { providers } from "@dwmkerr/ai-providers-and-models";

console.log(providers);
```

## Status

The following models have been validated:

| Model               | Status |
|---------------------|--------|
| **OpenAI**          |        |
| `gpt-4o-2024-08-06` | ✅     |
| `o3-mini-2025-01-31` | ✅     |


