from .base_client import BaseClient


class ItemClient(BaseClient):
    def create(self, wid, data):
        return self.post(f"/api/wishlists/{wid}/items/", files=data)

    def list(self, wid):
        return self.get(f"/api/wishlists/{wid}/items/")

    def update(self, wid, iid, data):
        return self.patch(f"/api/wishlists/{wid}/items/{iid}", json=data)

    def delete_one(self, wid, iid):
        return self.delete(f"/api/wishlists/{wid}/items/{iid}")
