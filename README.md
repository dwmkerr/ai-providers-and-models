# ai-providers-and-models

[![codecov](https://codecov.io/gh/dwmkerr/ai-providers-and-models/graph/badge.svg?token=1bEZ11ZqQZ)](https://codecov.io/gh/dwmkerr/ai-providers-and-models)
[![NPM Version](https://img.shields.io/npm/v/%40dwmkerr%2Fai-providers-and-models)](https://www.npmjs.com/package/@dwmkerr/ai-providers-and-models)
[![PyPI version](https://badge.fury.io/py/ai-providers-and-models.svg)](https://pypi.org/project/ai-providers-and-models/)

Regularly updated list of AI providers and models, available for multiple languages and platforms, such as [OpenAI](#status) and [Gemini](#status).

APIs available for:

| Language                             | Package                            |
|--------------------------------------|------------------------------------|
| [Python](./modules/python/README.md) | `ai_providers_and_models`          |
| [Node.JS](./modules/node/README.md)  | `@dwmkerr/ai-providers-and-models` |

> [!NOTE]
> This project is in the early stages, the API will most likely change. Please contribute or share if you can!

---

<!-- vim-markdown-toc GFM -->

- [Usage](#usage)
- [Features](#features)
- [APIs](#apis)
  - [NodeJS](#nodejs)
  - [Python](#python)
- [Status](#status)
- [Tips](#tips)

<!-- vim-markdown-toc -->

---

## Usage

The [`models.yaml`](./models.yaml) file contains details of available OpenAI models and their capabilities, you can [download it and use it directly](https://raw.githubusercontent.com/dwmkerr/ai-providers-and-models/refs/heads/main/models.yaml). There are also [Node.JS](#nodejs) and [Python](#python) APIs.

A short snippet is below - the `models.yaml` file is more complete.

```yaml
version: 0.1.9
updated: 2025-03-26T00:00:00.000Z
providers:
  openai:
    id: openai
    name: OpenAI
    docs: https://platform.openai.com/docs/models
    api_specification: api.openai.com/v1
    base_url: https://api.openai.com/v1/
    models:
      gpt-4o:
        id: gpt-4o
        name: GPT-4o
        documentation_url: https://platform.openai.com/docs/models/gpt-4o
        description_short: Fast, intelligent, flexible GPT model
        description: >-
          GPT-4o ("o" for "omni") is our versatile, high-intelligence flagship
          model. It accepts both text and image inputs, and produces text
          outputs (including Structured Outputs). It is the best model for most
          tasks, and is our most capable model outside of our o-series models.
        status: general-availability
        knowledgeCutoff: October 2023
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
          video: false
        endpoints:
          assistants: true
          batch: false
          chat_completions: true
          completions_legacy: false
          embeddings: false
          fine_tuning: true
          image_generation: false
          moderation: false
          realtime: false
          responses: true
          speech_generation: false
          transcription: false
          translation: false
        versions:
          - id: gpt-4o-2024-08-06
            release_date: "2024-08-06"
            isDefault: true
            isDeprecated: false
            description: Current version of GPT-4o, released August 2024
          - id: gpt-4o-2024-11-20
            release_date: "2024-11-20"
            isDefault: false
            isDeprecated: false
            description: Latest version of GPT-4o, released November 2024
          - id: gpt-4o-2024-05-13
            release_date: "2024-05-13"
            isDefault: false
            isDeprecated: true
            description: Previous version of GPT-4o, released May 2024 and now deprecated
```

## Features

- **Model Versioning**: Track multiple versions of models with deprecation status and default versions. See [versioning documentation](./modules/features.md#model-versioning) for details.
- **Provider Support**: Multiple AI providers including OpenAI and Gemini
- **Cross-Platform**: Available for Node.js and Python
- **Regular Updates**: Models and capabilities are regularly updated

## APIs

Model and provider data can be loaded programmatically for Node.JS and Python.

### NodeJS

Installation:

```bash
npm install @dwmkerr/ai-providers-and-models
```

Usage:

```javascript
import { providers } from "@dwmkerr/ai-providers-and-models";

//  Loop through each provider and its models...
for (const providerId of Object.keys(providers)) {
  const provider = providers[providerId];
  for (const modelId of Object.keys(provider.models)) {
    const model = provider.models[modelId];
    console.log(model.name);
  }
}

// ...or get more complex info!
const model = providers["openai"].models["gpt-4.5-preview"];
print(model.pricing.input_per_million)
```

Detailed documentation at: [modules/node/README.md](./modules/node/README.md)

### Python

Installation:

```bash
pip install ai_providers_and_models
```

Usage:

```python
from ai_providers_and_models import providers

# Loop through each provider and its models...
for provider in providers.values():
    print(provider.name)
    for model_id, model in provider.models.items():
        indent = "  "
        # Print the model name in green bold followed by a grey description.
        print(f"  {model.id} - {model.name}")

# ...or get more complex info!
model = providers["gemini"].models["models/gemini-2.0-flash"]
print(model.pricing.input_per_million)
print(model.modalities)
```

Detailed documentation at: [modules/python/README.md](./modules/python/README.md)

## Status

The following models have been validated:

- ✅ indicates that I have checked the features, pricing and context limits, however, there is always room for human error so be particularly careful and double check pricing.
- 🧠 indicates has been at least partly tested using [Terminal AI](https://github.com/dwmkerr/terminal-ai) and should work for chat and completion API calls.

| Name                                                                                        | Model                                                           | Status |
|---------------------------------------------------------------------------------------------|-----------------------------------------------------------------|--------|
| **OpenAI**                                                                                  |                                                                 |        |
| [GPT-4o](https://platform.openai.com/docs/models/gpt-4.1)                                   | `gpt-4.1-2025-04-14` (default)                                  | ✅ ⚠️  |
| [GPT-4o](https://platform.openai.com/docs/models/gpt-4o)                                    | `gpt-4o-2024-08-06` (default)                                   | ✅ 🧠  |
| [GPT-4.5 Preview](https://platform.openai.com/docs/models/gpt-4.5-preview)                  | `gpt-4.5-preview-2025-02-27` (default)                          | ✅ 🧠  |
| [ChatGPT o1](https://platform.openai.com/docs/models/o1)                                    | `o1-2024-12-17` (default)                                       | ✅ 🧠  |
| [ChatGPT o3-mini](https://platform.openai.com/docs/models/o3-mini)                          | `o3-mini-2025-01-31` (default)                                  | ✅ 🧠  |
| [ChatGPT o3-mini-high](https://platform.openai.com/docs/models/o3-mini)                     | `o3-mini-2025-01-31` (default) set `reasoning_effort` to `high` | ✅ 🧠  |
| [ChatGPT 4o mini](https://platform.openai.com/docs/models/gpt-4o-mini)                      | `gpt-4o-mini-2024-07-18` (default)                              | ✅ 🧠  |
| [ChatGPT 4](https://platform.openai.com/docs/models/gpt-4)                                  | `gpt-4-0613` (default)                                          | ✅ 🧠  |
| **Gemini**                                                                                  |                                                                 |        |
| [Gemini 2.0 Flash](https://ai.google.dev/gemini-api/docs/models#gemini-2.0-flash)           | `models/gemini-2.0-flash` (default)                             | ✅ 🧠  |
| [Gemini 2.0 Flash Lite](https://ai.google.dev/gemini-api/docs/models#gemini-2.0-flash-lite) | `models/gemini-2.0-flash-lite` (default)                        | ✅ 🧠  |
| [Gemini 1.5 Flash](https://ai.google.dev/gemini-api/docs/models#gemini-1.5-flash)           | `models/gemini-1.5-flash` (default)                             | ✅ 🧠  |

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
      - api_specification: api.openai.com/v1 # Gemini has an OpenAI compatible endpoint...
        base_url: https://generativelanguage.googleapis.com/v1beta/openai/
```
