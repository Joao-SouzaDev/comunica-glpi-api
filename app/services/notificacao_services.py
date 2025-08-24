import logging
import os
import requests
from dotenv import load_dotenv
import hashlib

load_dotenv()

CHATWOOT_API_URL = os.getenv("CHATWOOT_API_URL")
CHATWOOT_API_TOKEN = os.getenv("CHATWOOT_API_TOKEN")
CHATWOOT_ACCOUNT_ID = os.getenv("CHATWOOT_ACCOUNT_ID")

HEADERS = {"Content-Type": "application/json", "api_access_token": CHATWOOT_API_TOKEN}


def buscar_contato_por_telefone(phone_number):
    """
    Busca contato no Chatwoot pelo número de telefone.
    """
    url = f"{CHATWOOT_API_URL}/api/v1/accounts/{CHATWOOT_ACCOUNT_ID}/contacts/search"
    params = {"q": phone_number}
    response = requests.get(url, headers=HEADERS, params=params)
    logging.warning(
        f"Chatwoot API response: {response.status_code} | request: {response.request.url}"
    )
    if response.status_code == 200:
        data = response.json()
        if data.get("payload"):
            return data["payload"][0] if data["payload"] else None
        return None
    else:
        response.raise_for_status()


def criar_contato(nome, phone_number, email=None):
    """
    Cria um novo contato no Chatwoot.
    """
    url = f"{CHATWOOT_API_URL}/api/v1/accounts/{CHATWOOT_ACCOUNT_ID}/contacts"
    payload = {"name": nome, "phone_number": phone_number}
    if email:
        payload["email"] = email
    response = requests.post(url, headers=HEADERS, json=payload)
    if response.status_code in [200, 201]:
        return response.json()
    else:
        response.raise_for_status()


def iniciar_conversa(contact_id, inbox_id=None, additional_attributes=None):
    """
    Inicia uma nova conversa para um contato no Chatwoot.
    """
    url = f"{CHATWOOT_API_URL}/api/v1/accounts/{CHATWOOT_ACCOUNT_ID}/conversations"
    source_id = hashlib.sha256(str(contact_id).encode()).hexdigest()
    payload = {"contact_id": contact_id, "source_id": source_id}
    if inbox_id:
        payload["inbox_id"] = inbox_id
    if additional_attributes:
        payload["additional_attributes"] = additional_attributes
    response = requests.post(url, headers=HEADERS, json=payload)
    if response.status_code in [200, 201]:
        return response.json()
    else:
        response.raise_for_status()


def enviar_mensagem(conversation_id, message):
    """
    Envia uma mensagem para uma conversa no Chatwoot.
    """
    url = f"{CHATWOOT_API_URL}/api/v1/accounts/{CHATWOOT_ACCOUNT_ID}/conversations/{conversation_id}/messages"
    payload = {"content": message, "message_type": "outgoing"}
    response = requests.post(url, headers=HEADERS, json=payload)
    if response.status_code in [200, 201]:
        return response.json()
    else:
        response.raise_for_status()
