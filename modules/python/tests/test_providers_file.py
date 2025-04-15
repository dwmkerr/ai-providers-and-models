from datetime import date
import pytest
from src.ai_providers_and_models.providers_file import load_providers_file

TEST_YAML = """
version: "0.1.7"
updated: "2025-03-18"
source: "https://github.com/dwmkerr/ai-providers-and-models"
author: "dwmkerr"
providers:
  openai: &openai
    id: "openai"
    name: "OpenAI"
    docs: "https://platform.openai.com/docs/models"
    api_specification: "api.openai.com/v1"
    base_url: "https://api.openai.com/v1/"
    models:
      test-model:
        id: "test-model"
        name: "Test Model"
        documentation_url: "https://example.com/docs"
        description_short: "A test model"
        description: "This is a test model for demonstration purposes."
        status: "preview"
        knowledgeCutoff: "2024-01-01"
        context_window: 1024
        max_output_tokens: 512
        validated: true
        pricing:
          input_per_million: 1.0
          output_per_million: 2.0
        modalities:
          input:
            text: true
            image: false
            audio: false
            video: false
          output:
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
          - id: "test-model-2024-01-01"
            release_date: "2024-01-01"
            isDefault: true
            isDeprecated: false
            description: "Initial release of test model"
  # Google Gemini with the OpenAI Compatible Base URL.
  gemini_openai:
    <<: *openai
    id: gemini_openai
    name: Gemini (OpenAI Compatible)
    docs: https://ai.google.dev/gemini-api/docs/openai
"""


def test_load_providers_yaml(tmp_path):
    providers = load_providers_file(TEST_YAML)
    assert providers.version == "0.1.7"
    assert providers.updated == date(2025, 3, 18)
    assert providers.source == "https://github.com/dwmkerr/ai-providers-and-models"
    assert providers.author == "dwmkerr"

    assert "openai" in providers.providers
    openai_provider = providers.providers["openai"]
    assert openai_provider.name == "OpenAI"

    # Check one of the models
    test_model = openai_provider.models["test-model"]
    assert test_model.name == "Test Model"
    assert test_model.pricing.input_per_million == 1.0
    assert test_model.knowledgeCutoff == "2024-01-01"
    assert test_model.context_window == 1024
    assert test_model.max_output_tokens == 512
    assert test_model.validated is True

    # Check versions
    assert len(test_model.versions) == 1
    version = test_model.versions[0]
    assert version.id == "test-model-2024-01-01"
    assert version.release_date == "2024-01-01"
    assert version.isDefault is True
    assert version.isDeprecated is False
    assert version.description == "Initial release of test model"

    # Assert that we can load anchors (e.g. gemini_openai).
    gemini_openai = providers.providers["gemini_openai"]
    assert gemini_openai.id == "gemini_openai"
    assert gemini_openai.name == "Gemini (OpenAI Compatible)"
    assert gemini_openai.docs == "https://ai.google.dev/gemini-api/docs/openai"


def test_load_providers_yaml_invalid_yaml():
    with pytest.raises(RuntimeError, match="Invalid YAML syntax"):
        load_providers_file("invalid: yaml: {")


def test_load_providers_yaml_missing_required_fields():
    invalid_yaml = """
    version: "0.1.7"
    # missing updated field
    source: "https://github.com/dwmkerr/ai-providers-and-models"
    author: "dwmkerr"
    providers: {}
    """
    with pytest.raises(RuntimeError, match="Invalid data format"):
        load_providers_file(invalid_yaml)
