"""
Authentication handler for the API
Implements token-based authentication with permanent tokens
"""

from fastapi import HTTPException, Depends, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from typing import Optional
import os

# Security scheme
security = HTTPBearer()

# In production, this should be stored in environment variables or a secure database
# For now, using a single permanent token
VALID_TOKEN = os.getenv("API_TOKEN", "glpi-api-token-2025-permanent")


async def get_api_key(
    credentials: HTTPAuthorizationCredentials = Depends(security),
) -> str:
    """
    Validates the API token

    Args:
        credentials: HTTP Bearer token credentials

    Returns:
        str: The validated token

    Raises:
        HTTPException: If token is invalid
    """
    if credentials.credentials != VALID_TOKEN:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token inválido",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return credentials.credentials


def verify_token(token: str) -> bool:
    """
    Simple token verification

    Args:
        token: Token to verify

    Returns:
        bool: True if token is valid
    """
    return token == VALID_TOKEN
