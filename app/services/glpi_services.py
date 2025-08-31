import logging
import os
import requests
from typing import Any, Dict, Optional
from dotenv import load_dotenv

load_dotenv()
logging.basicConfig(level=logging.INFO)
GLPI_API_URL = os.getenv("GLPI_API_URL")
GLPI_APP_TOKEN = os.getenv("GLPI_APP_TOKEN")
GLPI_USER_TOKEN = os.getenv("GLPI_USER_TOKEN")


class GLPIService:
    def __init__(self):
        self.api_url = GLPI_API_URL
        self.app_token = GLPI_APP_TOKEN
        self.user_token = GLPI_USER_TOKEN
        self.session_token: Optional[str] = None

    def _get_headers(self, with_session: bool = True) -> Dict[str, str]:
        headers = {"App-Token": self.app_token, "Content-Type": "application/json"}
        if with_session and self.session_token:
            headers["Session-Token"] = self.session_token
        elif not with_session:
            headers["Authorization"] = f"user_token {self.user_token}"
        return headers

    def init_session(self) -> None:
        url = f"{self.api_url}/initSession"
        logging.info(f"Initializing session with URL: {url}")
        headers = {
            "App-Token": self.app_token,
            "Authorization": f"user_token {self.user_token}",
        }
        response = None
        try:
            response = requests.get(url, headers=headers)
            response.raise_for_status()
            self.session_token = response.json().get("session_token")
        except requests.RequestException as e:
            logging.error(f"Erro ao iniciar sessão: {e}")
            if response is not None:
                logging.error(f"Resposta do servidor: {response.text}")
            raise

    def kill_session(self) -> None:
        if not self.session_token:
            return
        url = f"{self.api_url}/killSession"
        headers = self._get_headers()
        response = None
        try:
            response = requests.get(url, headers=headers)
            response.raise_for_status()
        except requests.RequestException as e:
            logging.error(f"Erro ao finalizar sessão: {e}")
            if response is not None:
                logging.error(f"Resposta do servidor: {response.text}")
            raise
        self.session_token = None

    def get(self, endpoint: str, params: Optional[Dict[str, Any]] = None) -> Any:
        if not self.session_token:
            self.init_session()
        url = f"{self.api_url}/{endpoint}"
        headers = self._get_headers()
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()
        return response.json()

    def post(self, endpoint: str, data: Dict[str, Any]) -> Any:
        if not self.session_token:
            self.init_session()
        url = f"{self.api_url}/{endpoint}"
        headers = self._get_headers()
        response = None
        try:
            response = requests.post(url, headers=headers, json=data)
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            logging.error(f"Erro ao fazer POST para {url}: {e}")
            if response is not None:
                logging.error(f"Resposta do servidor: {response.text}")
            raise

    def put(self, endpoint: str, data: Dict[str, Any]) -> Any:
        if not self.session_token:
            self.init_session()
        url = f"{self.api_url}/{endpoint}"
        headers = self._get_headers()
        response = requests.put(url, headers=headers, json=data)
        response.raise_for_status()
        return response.json()

    def delete(self, endpoint: str) -> Any:
        if not self.session_token:
            self.init_session()
        url = f"{self.api_url}/{endpoint}"
        headers = self._get_headers()
        response = requests.delete(url, headers=headers)
        response.raise_for_status()
        return response.json()
