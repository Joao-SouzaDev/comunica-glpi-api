import os
import requests
from typing import Any, Dict, Optional
from dotenv import load_dotenv

load_dotenv()

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
        headers = {
            "App-Token": self.app_token,
            "Authorization": f"user_token {self.user_token}",
        }
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        self.session_token = response.json().get("session_token")

    def kill_session(self) -> None:
        if not self.session_token:
            return
        url = f"{self.api_url}/killSession"
        headers = self._get_headers()
        requests.get(url, headers=headers)
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
        response = requests.post(url, headers=headers, json=data)
        response.raise_for_status()
        return response.json()

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
