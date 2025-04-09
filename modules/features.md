# Features

This document explains the key features of the AI Providers and Models library.

## Model Versioning

Models can have multiple versions, each with its own release date, deprecation status, and default status. Here's an example from the YAML:

```yaml
models:
  gpt-4o:
    id: gpt-4o
    versions:
      - id: gpt-4o-2024-08-06
        release_date: "2024-08-06"
        isDefault: true
        isDeprecated: false
        description: Current version of GPT-4o
      - id: gpt-4o-2024-05-13
        release_date: "2024-05-13"
        isDefault: false
        isDeprecated: true
        description: Previous version of GPT-4o
```

### Using Versions in Python

```python
from ai_providers_and_models import providers

# Get a model
model = providers["openai"].models["gpt-4o"]

# Get the default version
default_version = next(v for v in model.versions if v.isDefault)
print(f"Default version: {default_version.id}")

# List all versions
for version in model.versions:
    print(f"{version.id} (default: {version.isDefault}, deprecated: {version.isDeprecated})")

# Get the latest non-deprecated version
latest = next(v for v in model.versions if not v.isDeprecated)
print(f"Latest version: {latest.id}")
```

### Using Versions in Node.js

```javascript
import { providers } from "@dwmkerr/ai-providers-and-models";

// Get a model
const model = providers["openai"].models["gpt-4o"];

// Get the default version
const defaultVersion = model.versions.find(v => v.isDefault);
console.log(`Default version: ${defaultVersion.id}`);

// List all versions
model.versions.forEach(version => {
    console.log(`${version.id} (default: ${version.isDefault}, deprecated: ${version.isDeprecated})`);
});

// Get the latest non-deprecated version
const latest = model.versions.find(v => !v.isDeprecated);
console.log(`Latest version: ${latest.id}`);
```

### Version Properties

Each version has the following properties:

- `id`: The unique identifier for the version
- `release_date`: The date the version was released (YYYY-MM-DD format)
- `isDefault`: Whether this is the default version of the model
- `isDeprecated`: Whether this version is deprecated
- `description`: A description of the version

## Provider Support

The library supports multiple AI providers, including OpenAI and Gemini. Each provider can have:

- Multiple models
- Custom API specifications
- Additional endpoints (e.g., OpenAI-compatible endpoints for Gemini)
- Provider-specific documentation

## Cross-Platform Support

The library is available for both Node.js and Python, with consistent APIs across platforms. See the [Python](./python/README.md) and [Node.js](./node/README.md) documentation for platform-specific details. 