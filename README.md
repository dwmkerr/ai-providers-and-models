# ai-providers-and-models

Work in progress. Regularly updated list of AI providers and models, available for multiple languages and platforms.

I'm looking for help! Please do contribute if you think this would be useful!

Important:

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
version: 0.1.5
updated: 2025-03-12T00:00:00.000Z
providers:
  openai:
    id: openai
    name: OpenAI
    docs: https://platform.openai.com/docs/models
    api_specification: openai/v1
    models:
      "gpt-4o-2024-08-06":
        id: gpt-4o-2024-08-06
        name: GPT-4o
        documentation_url: https://platform.openai.com/docs/models/gpt-4o
        description_short: Fast, intelligent, flexible GPT model
        description: >-
          GPT-4o (“o” for “omni”) is our versatile, high-intelligence flagship
          model. It accepts both text and image inputs, and produces text
          outputs (including Structured Outputs). It is the best model for most
          tasks, and is our most capable model outside of our o-series models.
        status: general-availability
        knowledge_cutoff: September 30, 2023
        context_window: 128000
        max_output_tokens: 16384 
        validated: true
        pricing:
          input_per_million: 2.5
          output_per_million: 10
        modalities:
          text: true
          image: false
          audio: false
        endpoints:
          assistants: true
          # ...etc...
```

## NodeJS

Installation:

```bash
npm install @dwmkerr/ai-providers-and-models
```

Usage:

```javascript
import { providers } from "@dwmkerr/ai-providers-and-models";

//  Retrieve a specific model by provider and model id.
const model = providers["openai"].models["gpt-4.5-preview"];
console.log(model);

//  Loop through all providers and models.
for (const providerId of Object.keys(providers)) {
  const provider = providers[providerId];
  for (const modelId of Object.keys(provider.models)) {
    const model = provider.models[modelId];
    console.log(provider.name + " " + model.name);
  }
}
```

## Status

The following models have been validated:

- ✅ indicates that I have checked the features, pricing and context limits, however, there is always room for human error so be particularly careful and double check pricing.
- 🧠 indicates has been at least partly tested using [Terminal AI](https://github.com/dwmkerr/terminal-ai) and should work for chat and completion API calls.

| Name                                                                       | Model                                    | Status                  |
|----------------------------------------------------------------------------|------------------------------------------|-------------------------|
| **OpenAI**                                                                 |                                          |                         |
| [GPT-4o](https://platform.openai.com/docs/models/gpt-4o)                   | `gpt-4o-2024-08-06` (default)            | ✅ 🧠                   |
| [GPT-4.5 Preview](https://platform.openai.com/docs/models/gpt-4.5-preview) | `gpt-4.5-preview-2025-02-27` (default)   | ⚠️  (Testing in Process) |
| ChatGPT o1](https://platform.openai.com/docs/models/o1)                    | `o1-2024-12-17` (default)                | ✅ 🧠                  |
| ChatGPT o3-mini                                                            |                                          | ❌                      |
| ChatGPT o3-mini                                                            |                                          | ❌                      |
| ChatGPT o3-mini-high                                                       |                                          | ❌                      |
| ChatGPT 4o mini                                                            |                                          | ❌                      |
| ChatGPT 4                                                                  |                                          | ❌                      |
| [o3-mini](https://platform.openai.com/docs/models/o3-mini)                 | `o3-mini-2025-01-31`           (default) | ✅                      |


