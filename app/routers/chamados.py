"""
Chamados (Tickets) router
Handles all ticket-related operations with authentication
"""

import logging
from fastapi import APIRouter, Depends
from typing import Dict, List, Any
from app.auth.auth_handler import get_api_key
from app.services.ticket_services import TicketServices

router = APIRouter()
ticket_services = TicketServices()
logging.basicConfig(level=logging.INFO)


@router.get("/chamados")
async def listar_chamados(token: str = Depends(get_api_key)) -> Dict[str, Any]:
    """
    Lista todos os chamados
    Requires authentication

    Args:
        token: API token (injected by dependency)

    Returns:
        Dict: List of tickets
    """
    # Placeholder implementation
    return {
        "message": "Lista de chamados",
        "data": [],
        "total": 0,
        "authenticated": True,
    }


@router.get("/chamados/{chamado_id}")
async def obter_chamado(
    chamado_id: int, token: str = Depends(get_api_key)
) -> Dict[str, Any]:
    """
    Obtém um chamado específico por ID
    Requires authentication

    Args:
        chamado_id: ID do chamado
        token: API token (injected by dependency)

    Returns:
        Dict: Ticket details
    """
    # Placeholder implementation
    return {
        "message": f"Detalhes do chamado {chamado_id}",
        "data": {
            "id": chamado_id,
            "titulo": "Chamado exemplo",
            "status": "Em andamento",
        },
        "authenticated": True,
    }


@router.post("/chamados")
async def criar_chamado(
    chamado_data: Dict[str, Any], token: str = Depends(get_api_key)
) -> Dict[str, Any]:
    """
    Cria um novo chamado
    Requires authentication

    Args:
        chamado_data: Dados do chamado a ser criado
        token: API token (injected by dependency)

    Returns:
        Dict: Created ticket information
    """
    logging.info(f"Criando chamado com dados: {chamado_data}")
    response = ticket_services.create_ticket(chamado_data)

    if isinstance(response, dict) and "error" in response:
        return {
            "message": "Erro ao criar chamado",
            "error": response["error"],
            "authenticated": True,
        }

    return {
        "message": "Chamado criado com sucesso",
        "data": response,
        "authenticated": True,
    }
