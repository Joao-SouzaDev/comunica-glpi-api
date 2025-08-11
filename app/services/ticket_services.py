from services import glpi_services
from typing import Any, Dict, Optional


class TicketServices(glpi_services.GLPIService):
    def __init__(self):
        super().__init__()

    def create_ticket(self, ticket_data: Dict[str, Any]) -> Any:
        return self.post("ticket", data=ticket_data)

    def get_ticket(self, ticket_id: int) -> Any:
        return self.get(f"ticket/{ticket_id}")

    def update_ticket(self, ticket_id: int, ticket_data: Dict[str, Any]) -> Any:
        return self.put(f"ticket/{ticket_id}", data=ticket_data)

    def delete_ticket(self, ticket_id: int) -> Any:
        return self.delete(f"ticket/{ticket_id}")
