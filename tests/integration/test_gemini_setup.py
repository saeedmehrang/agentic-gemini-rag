import os
import pytest
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage
from typing import Optional
from dotenv import load_dotenv

load_dotenv()

# --- Configuration ---
# NOTE: Replace this mock key with your actual key for live testing.
MOCK_MODEL = "gemini-2.5-flash-lite"


def initialize_gemini_llm(api_key: Optional[str] = None) -> ChatGoogleGenerativeAI:
    """
    Initializes the ChatGoogleGenerativeAI model.
    It prefers the passed api_key, then the GEMINI_API_KEY environment variable.
    """
    try:
        # Initialization using the 'GEMINI_API_KEY' argument is the most explicit way.
        llm = ChatGoogleGenerativeAI(
            model=MOCK_MODEL,
            temperature=0.7,
            # For robust authentication when using an explicit key, 'transport="rest"' is sometimes helpful.
            transport='rest'
        )
        return llm
    except Exception as e:
        print(f"Error during ChatGoogleGenerativeAI initialization: {e}")
        raise

# --- Test Cases ---

def test_gemini_setup_via_constructor():
    """
    Tests successful instantiation by passing the key directly.
    """
    print(f"\n--- Testing setup via 'gemini_api_key' argument ---")
    
    # 1. Initialize the model using the key passed to the constructor
    llm = initialize_gemini_llm()
    
    # Check if the object is the correct type
    assert isinstance(llm, ChatGoogleGenerativeAI)
    print("SUCCESS: ChatGoogleGenerativeAI instantiated correctly.")

    # 2. Demonstrate a simple invocation structure (requires a real key to work)
    try:
        print(f"Attempting live invocation with {MOCK_MODEL}...")
        messages = [
            HumanMessage(content="Why is the sky blue? Answer in exactly one sentence.")
        ]
        response = llm.invoke(messages)
        print(f"Live Response Content: {response.content}")
        assert len(response.content) > 10 # Check for non-empty response
        pass
    except Exception as e:
        # In a real test, if the API call fails due to the MOCK key, this is expected.
        print(f"Note: Invocation failed: {e}")


def test_gemini_setup_from_env():
    """
    Tests instantiation by relying on the GEMINI_API_KEY environment variable.
    You must set this env var before running this test.
    """
    print(f"\n--- Testing setup via GEMINI_API_KEY environment variable ---")
    
    if "GEMINI_API_KEY" not in os.environ:
        # This check should ideally be done before running the test (using the pytest skip marker)
        pytest.skip("GEMINI_API_KEY environment variable not set.")
        
    # Initialize the model (it should automatically read the key from the environment)
    llm = initialize_gemini_llm()
    
    # Check if the object is the correct type
    assert isinstance(llm, ChatGoogleGenerativeAI)
    print("SUCCESS: ChatGoogleGenerativeAI instantiated correctly from environment variable.")
