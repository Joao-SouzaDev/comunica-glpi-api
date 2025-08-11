"""
Health check router
Provides endpoints for API health monitoring
"""

from fastapi import APIRouter
from datetime import datetime
from typing import Dict, Any

router = APIRouter()


@router.get("/health")
async def health_check() -> Dict[str, Any]:
    """
    Health check endpoint

    Returns:
        Dict: Health status information
    """
    return {
        "status": "healthy",
        "timestamp": datetime.now().isoformat(),
        "service": "Comunica GLPI API",
        "version": "1.0.0",
    }


@router.get("/health/detailed")
async def detailed_health_check() -> Dict[str, Any]:
    """
    Detailed health check endpoint

    Returns:
        Dict: Detailed health status information
    """
    return {
        "status": "healthy",
        "timestamp": datetime.now().isoformat(),
        "service": "Comunica GLPI API",
        "version": "1.0.0",
        "environment": "development",
        "uptime": "N/A",  # Could be implemented with app startup time
        "dependencies": {
            "database": "not_implemented",
            "glpi_connection": "not_implemented",
        },
    }
