#!/usr/bin/env python3
"""
OpenAI Model Integration Tests

This script tests OpenAI models defined in the ai_providers_and_models package
by attempting to initialize and use each model with the OpenAI Python SDK.

The tests verify that models can be initialized with the OpenAI SDK and that a
simple completion can be executed.

Requirements:
- openai (pip install openai)

Environment Variables:
- OPENAI_API_KEY: Required. Your API key for OpenAI.
- OPENAI_BASE_URL: Optional. Custom base URL for API requests.
"""

import os
import sys
from typing import Dict, List, Tuple, Set

# Add python directory to path so we can import the package
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../python')))
from ai_providers_and_models import providers

from openai import OpenAI

# ANSI color codes for terminal output
GREEN = "\033[92m"
RED = "\033[91m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
CYAN = "\033[96m"
RESET = "\033[0m"
BOLD = "\033[1m"


def get_openai_models_from_yaml() -> List[Tuple[str, Dict]]:
    """Get all OpenAI models from the providers file."""
    if 'openai' not in providers:
        print("error: OpenAI provider not found in configuration")
        return []
    
    openai_provider = providers['openai']
    models = [(model_id, model) for model_id, model in openai_provider.models.items()]
    
    return models


def get_openai_models_from_api(client: OpenAI) -> Set[str]:
    """Get all available model IDs from the OpenAI API."""
    try:
        response = client.models.list()
        return {model.id for model in response.data}
    except Exception as e:
        print(f"error: failed to fetch models from OpenAI API: {str(e)}")
        return set()


def test_model(model_id: str, model_info: Dict, client: OpenAI) -> bool:
    """Test a single OpenAI model and return success status."""
    try:
        # Construct a simple prompt
        prompt = "What are the main features of this model? Answer in one sentence."
        
        # Make completion request
        messages = [{"role": "user", "content": prompt}]
        client.chat.completions.create(
            model=model_id,
            messages=messages,
        )
        
        return True
    except Exception as e:
        print(f"  {RED}error testing {model_id}: {str(e)}{RESET}")
        return False


def color_check(value: bool) -> str:
    """Return a colored checkmark or X based on the boolean value."""
    if value:
        return f"{GREEN}✓{RESET}"
    return f"{RED}✗{RESET}"


def print_model_tree(model_id: str, model, in_api: bool, test_result: bool = None):
    """Print a model and its versions in a tree-like structure."""
    # Determine the status mark for the main model
    if test_result is not None:
        status_mark = color_check(test_result)
    elif not in_api:
        status_mark = f"{RED}✗{RESET}"  # Not in API
    else:
        status_mark = f"{YELLOW}?{RESET}"  # In API but not tested
    
    # Print the main model line with validation mark if needed
    validated_str = f" {GREEN}(validated){RESET}" if model.validated else ""
    print(f"{status_mark} {model_id}{validated_str}")
    
    # Print version information if available
    if model.versions:
        for version in model.versions:
            # Determine the version status
            version_status = []
            if version.isDefault:
                version_status.append(f"{GREEN}(default){RESET}")
            if version.isDeprecated:
                version_status.append(f"{RED}(deprecated){RESET}")
            
            version_status_str = " ".join(version_status)
            
            # Check if this specific version is in the API
            version_in_api = version.id in api_models
            version_mark = color_check(version_in_api)
            
            # Indent and print version
            print(f"  {version_mark} {version.id} {version_status_str}")
    
    # Add a visual separator between models
    print()


def main():
    # Check for API key
    api_key = os.environ.get("OPENAI_API_KEY")
    if not api_key:
        print("error: OPENAI_API_KEY environment variable not set")
        sys.exit(1)
    
    # Check for optional base URL
    base_url = os.environ.get("OPENAI_BASE_URL")
    
    # Initialize OpenAI client with base URL if provided
    client_params = {"api_key": api_key}
    if base_url:
        client_params["base_url"] = base_url
        print(f"info: using custom base URL: {base_url}")
    
    client = OpenAI(**client_params)
    
    # Get models from both sources
    yaml_models = get_openai_models_from_yaml()
    global api_models
    api_models = get_openai_models_from_api(client)
    
    if not yaml_models:
        print("error: no OpenAI models found in configuration")
        sys.exit(1)
    
    # Get model IDs from YAML for comparison
    yaml_model_ids = {model_id for model_id, _ in yaml_models}
    
    # Create a dictionary to track test results
    test_results = {}
    
    # Find models in YAML but not in API and vice versa
    yaml_only_models = yaml_model_ids - api_models
    api_only_models = api_models - yaml_model_ids
    
    # Print header
    print(f"\n{BOLD}OpenAI Models Integration Test{RESET}")
    print("-" * 60)
    
    # Test all models from YAML that are available in the API
    print(f"{YELLOW}Testing models...{RESET}")
    for model_id, model in yaml_models:
        if model_id in api_models and (not model.versions or not all(v.isDeprecated for v in model.versions)):
            print(f"  testing {model_id}...")
            test_results[model_id] = test_model(model_id, model, client)
    
    print(f"\n{BOLD}Models from YAML Configuration:{RESET}")
    print("-" * 60)
    
    # Print model tree for all models in YAML
    for model_id, model in yaml_models:
        in_api = model_id in api_models
        test_status = test_results.get(model_id) if in_api else None
        print_model_tree(model_id, model, in_api, test_status)
    
    # Print summary info
    print(f"{BOLD}Summary:{RESET}")
    print(f"total models in yaml: {len(yaml_models)}")
    print(f"total models in api: {len(api_models)}")
    print(f"models in yaml but not in api: {len(yaml_only_models)}")
    print(f"models in api but not in yaml: {len(api_only_models)}")
    
    # Don't print out the names of untested models, just the count
    if api_only_models:
        print(f"{YELLOW}note: {len(api_only_models)} api models not tested{RESET}")
    
    # Count successful tests
    successful = sum(1 for result in test_results.values() if result)
    testable = len(test_results)
    
    # Print test results
    print(f"\n{BOLD}Test Results:{RESET}")
    print(f"tested models: {testable}")
    print(f"successful tests: {GREEN}{successful}/{testable}{RESET}")
    
    # Exit with error code if any tests failed
    if successful < testable:
        sys.exit(1)


if __name__ == "__main__":
    main()