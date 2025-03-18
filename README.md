# ai-providers-and-models

Regularly updated list of AI providers and models, available for multiple languages and platforms, including:

- OpenAI
- Gemini

> [!CAUTION]
> This project is in the early stages, the API will most likely change. Please contribute or share if you can!

<!-- vim-markdown-toc GFM -->

- [Usage](#usage)
- [NodeJS](#nodejs)
- [Status](#status)
- [Tips](#tips)

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

| Name                                                                                        | Model                                                           | Status                  |
|---------------------------------------------------------------------------------------------|-----------------------------------------------------------------|-------------------------|
| **OpenAI**                                                                                  |                                                                 |                         |
| [GPT-4o](https://platform.openai.com/docs/models/gpt-4o)                                    | `gpt-4o-2024-08-06` (default)                                   | ✅ 🧠                   |
| [GPT-4.5 Preview](https://platform.openai.com/docs/models/gpt-4.5-preview)                  | `gpt-4.5-preview-2025-02-27` (default)                          | ⚠️  (Testing in Process) |
| [ChatGPT o1](https://platform.openai.com/docs/models/o1)                                    | `o1-2024-12-17` (default)                                       | ✅ 🧠                   |
| [ChatGPT o3-mini](https://platform.openai.com/docs/models/o3-mini)                          | `o3-mini-2025-01-31` (default)                                  | ✅ 🧠                   |
| [ChatGPT o3-mini-high](https://platform.openai.com/docs/models/o3-mini)                     | `o3-mini-2025-01-31` (default) set `reasoning_effort` to `high` | ✅ 🧠                   |
| [ChatGPT 4o mini](https://platform.openai.com/docs/models/gpt-4o-mini)                      | `gpt-4o-mini-2024-07-18` (default)                              | ✅ 🧠                   |
| [ChatGPT 4](https://platform.openai.com/docs/models/gpt-4)                                  | `gpt-4-0613` (default)                                          | ❌                      |
| **Gemini**                                                                                  |                                                                 |                         |
| [Gemini 2.0 Flash](https://ai.google.dev/gemini-api/docs/models#gemini-2.0-flash)           | `models/gemini-2.0-flash` (default)                             | ⚠️  (Testing in Process) |
| [Gemini 2.0 Flash Lite](https://ai.google.dev/gemini-api/docs/models#gemini-2.0-flash-lite) | `models/gemini-2.0-flash-lite` (default)                        | ⚠️  (Testing in Process) |
| [Gemini 1.5 Flash](https://ai.google.dev/gemini-api/docs/models#gemini-1.5-flash)           | `models/gemini-1.5-flash` (default)                             | ⚠️  (Testing in Process) | 

Notes:

**o3-mini-high**

This model is simply **o3-mini** with `reasoning_effort` set to `high`.

Details: https://community.openai.com/t/is-03-mini-in-the-api-the-low-medium-or-high-version/1110423/2

## Tips

**Handling OpenAI Compatible Endpoints**

Some providers offer additional endpoints are compatible with OpenAI, for example [Google Gemini OpenAI Compatiblity](https://ai.google.dev/gemini-api/docs/openai). This is reflected in the YAML like so:

```yaml
providers:
  gemini:
    id: gemini
    api_specification: generativelanguage.googleapis.com/v1beta
    base_url: https://generativelanguage.googleapis.com/v1beta/
    additional_endpoints:
      # Gemini has OpenAI compatible endpoints.
      # https://ai.google.dev/gemini-api/docs/openai
      api_specification: api.openai.com/v1
      base_url: https://generativelanguage.googleapis.com/v1beta/openai/
```

NodeJS Example:


