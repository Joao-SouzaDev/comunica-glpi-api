import logging
from fastapi import APIRouter, Depends, HTTPException, status
from pydantic import BaseModel


class MensagemRequest(BaseModel):
    message: str
    phone: str


from typing import Optional
from app.services import notificacao_services

logging.basicConfig(level=logging.INFO)


# Dependência de autenticação (implemente conforme seu projeto)
def get_api_token():
    # Exemplo: verificação simples via header ou token fixo
    # Implemente conforme sua lógica de autenticação
    pass


router = APIRouter(
    prefix="/notificacao", tags=["Notificação"], dependencies=[Depends(get_api_token)]
)


@router.get("/contato")
def buscar_contato(phone_number: str):
    contato = notificacao_services.buscar_contato_por_telefone(phone_number)
    if not contato:
        raise HTTPException(status_code=404, detail="Contato não encontrado")
    return contato


@router.post("/contato")
def criar_contato(nome: str, phone_number: str, email: Optional[str] = None):
    contato = notificacao_services.criar_contato(nome, phone_number, email)
    return contato


@router.post("/conversa")
def iniciar_conversa(
    contact_id: int,
    inbox_id: Optional[int] = None,
    additional_attributes: Optional[dict] = None,
):
    conversa = notificacao_services.iniciar_conversa(
        contact_id, inbox_id, additional_attributes
    )
    return conversa


@router.post("/mensagem")
def enviar_mensagem(request: MensagemRequest):
    contato = notificacao_services.buscar_contato_por_telefone(request.phone)
    if not contato:
        raise HTTPException(status_code=404, detail="Contato não encontrado")
    logging.info(f"Criando conversa para contato {contato['id']}")
    conversation_id = notificacao_services.iniciar_conversa(contato["id"], 1)
    if not conversation_id:
        raise HTTPException(
            status_code=400, detail="Não foi possível iniciar a conversa"
        )
    logging.info(f"Enviando mensagem para a conversa {conversation_id['id']}")
    resposta = notificacao_services.enviar_mensagem(
        conversation_id["id"], request.message
    )
    return resposta
