from .base_client import BaseClient


class ReservationClient(BaseClient):
    def create(self, data):
        return self.post("/api/reservations/", json=data)

    def cancel(self, rid):
        return self.delete(f"/api/reservations/{rid}")
