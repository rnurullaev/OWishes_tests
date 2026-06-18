import requests

from config import Config


class BaseClient:
    def __init__(self):
        self.session = requests.Session()

    def auth(self, token):
        self.session.headers.update({"Authorization": f"Bearer {token}"})

    def get(self, path):
        return self.session.get(Config.API_URL + path)

    def post(self, path, **kwargs):
        return self.session.post(Config.API_URL + path, **kwargs)

    def patch(self, path, **kwargs):
        return self.session.patch(Config.API_URL + path, **kwargs)

    def delete(self, path):
        return self.session.delete(Config.API_URL + path)
