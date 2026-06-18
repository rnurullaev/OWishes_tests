from .base_client import BaseClient


class AuthClient(BaseClient):
    def register(self, data):
        return self.post("/api/auth/register", json=data)

    def login(self, email, password):
        return self.post(
            "/api/auth/login", json={"username": email, "password": password}
        )

    def me(self):
        return self.get("/api/auth/me")
