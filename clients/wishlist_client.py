from .base_client import BaseClient


class WishlistClient(BaseClient):
    def list(self):
        return self.get("/api/wishlists/")

    def create(self, data):
        return self.post("/api/wishlists/", json=data)

    def get_one(self, wid):
        return self.get(f"/api/wishlists/{wid}")

    def update(self, wid, data):
        return self.patch(f"/api/wishlists/{wid}", json=data)

    def delete_one(self, wid):
        return self.delete(f"/api/wishlists/{wid}")
