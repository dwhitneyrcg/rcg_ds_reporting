"""OpenAI embedding model wrapper. Client is created once per process."""

from __future__ import annotations
from dotenv import load_dotenv
load_dotenv()  # Load environment variables from .env if present
import os

MODEL_NAME = "text-embedding-3-small"
DIMENSION = 1536

_client = None


def get_client():
    global _client
    if _client is None:
        from openai import OpenAI
        _client = OpenAI(api_key=os.environ["API_KEY"])
    return _client


def embed(text: str) -> list[float]:
    """Embed text and return a normalized float vector (length 1536)."""
    response = get_client().embeddings.create(
        model=MODEL_NAME,
        input=text,
    )
    return response.data[0].embedding
