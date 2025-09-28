from app.services.glpi_services import GLPIService
from typing import Any, Dict


class TicketServices(GLPIService):
    def __init__(self):
        super().__init__()

    def create_ticket(self, ticket_data: Dict[str, Any]) -> Any:
        try:
            return self.post("Ticket", data=ticket_data)
        except Exception as e:
            return {"error": str(e)}

    def get_ticket(self, ticket_id: int) -> Any:
        try:
            return self.get(f"Ticket/{ticket_id}")
        except Exception as e:
            return {"error": str(e)}

    def update_ticket(self, ticket_id: int, ticket_data: Dict[str, Any]) -> Any:
        try:
            return self.put(f"Ticket/{ticket_id}", data=ticket_data)
        except Exception as e:
            return {"error": str(e)}

    def delete_ticket(self, ticket_id: int) -> Any:
        try:
            return self.delete(f"Ticket/{ticket_id}")
        except Exception as e:
            return {"error": str(e)}

    def add_followup(self, followup_data: Dict[str, Any]) -> Any:
        try:
            return self.post(f"ITILFollowup", data=followup_data)
        except Exception as e:
            return {"error": str(e)}
