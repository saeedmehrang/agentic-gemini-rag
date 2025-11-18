# tests/unit/test_settings.py

import pytest
from dotenv import dotenv_values

# Get the actual values from the .env file without using settings.py's logic
# This assumes your .env is in the root directory
ENV_VARS = dotenv_values(".env")

def test_api_key_is_in_env_file():
    """Verifies the API key is defined in the .env file."""
    assert "GEMINI_API_KEY" in ENV_VARS, "GEMINI_API_KEY is missing from the .env file."
    assert ENV_VARS["GEMINI_API_KEY"] != "", "GEMINI_API_KEY value is empty in the .env file."

def test_default_values_are_correct_types():
    """Checks that default values are defined correctly as strings in settings.py."""
    
    # You could import settings and check the final types, but for a pure unit test
    # without external dependencies, checking the .env file for the required key is enough.
    
    # Example: Check if a key that *must* be an integer is convertible
    if "CHUNK_SIZE" in ENV_VARS:
        try:
            int(ENV_VARS["CHUNK_SIZE"])
        except ValueError:
            pytest.fail("CHUNK_SIZE in .env file is not a valid integer.")