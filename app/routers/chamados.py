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
    data_chamado = ticket_services.get_ticket(chamado_id)

    # Log para debug da estrutura dos dados
    logging.info(f"Dados retornados da API GLPI: {data_chamado}")
    logging.info(f"Tipo dos dados: {type(data_chamado)}")

    if data_chamado is None or (
        isinstance(data_chamado, dict) and "error" in data_chamado
    ):
        return {
            "message": "Chamado não encontrado",
            "error": (
                data_chamado.get("error") if isinstance(data_chamado, dict) else None
            ),
            "authenticated": True,
        }

    # Verifica a estrutura dos dados retornados e processa o status
    if isinstance(data_chamado, dict):
        # Se existe uma chave "data" com os dados do ticket
        if "data" in data_chamado and isinstance(data_chamado["data"], dict):
            status_code = data_chamado["data"].get("status", 0)
            data_chamado["data"]["status"] = enumerate_status(status_code)
        # Se os dados estão diretamente no objeto retornado
        elif "status" in data_chamado:
            status_code = data_chamado.get("status", 0)
            data_chamado["status"] = enumerate_status(status_code)
        # Se o retorno é uma lista (alguns endpoints do GLPI retornam arrays)
        elif isinstance(data_chamado, list) and len(data_chamado) > 0:
            for item in data_chamado:
                if isinstance(item, dict) and "status" in item:
                    status_code = item.get("status", 0)
                    item["status"] = enumerate_status(status_code)

    return {
        "message": "Chamado encontrado",
        "data": data_chamado,
        "authenticated": True,
    }


def enumerate_status(status_code: int) -> str:
    status_mapping = {
        1: "Novo",
        2: "Em andamento",
        3: "Fechado",
        4: "Pendente",
        5: "Resolvido",
    }
    return status_mapping.get(status_code, "Desconhecido")


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


@router.post("/chamados/followup")
async def adicionar_followup(
    followup_data: Dict[str, Any], token: str = Depends(get_api_key)
) -> Dict[str, Any]:
    """
    Adiciona um follow-up a um chamado existente
    Requires authentication

    Args:
        chamado_id: ID do chamado ao qual o follow-up será adicionado
        followup_data: Dados do follow-up a ser adicionado
        token: API token (injected by dependency)

    Returns:
        Dict: Follow-up information
    """
    logging.info(
        f"Adicionando follow-up ao chamado {followup_data.get('items_id')} com dados: {followup_data}"
    )
    response = ticket_services.add_followup(followup_data)

    if isinstance(response, dict) and "error" in response:
        return {
            "message": "Erro ao adicionar follow-up",
            "error": response["error"],
            "authenticated": True,
        }

    return {
        "message": "Follow-up adicionado com sucesso",
        "data": response,
        "authenticated": True,
    }
