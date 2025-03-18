from typing import Any
import requests
from odata import ODataService
from requests.auth import HTTPBasicAuth

from pyaimairaodata import Entity


class OData:

    def __init__(
        self,
        url,
        email,
        password
    ):
        self.url = url
        self.service = ODataService(
            url=url,
            auth=HTTPBasicAuth(email, password),
            reflect_entities=True
        )

    def __repr__(self):
        return f"OData pour l'url {self.url}"

    def get_entities(self, universe=None):
        if universe is None:
            return self.service.entities
        else:
            return {name: entity for name, entity in self.service.entities.items() if name.startswith(universe.value)}

    def get(self, name):
        return Entity(
            entity=self.get_entities()[name],
            odata=self
        )

    def __getitem__(self, key):
        return self.get(key)

    def query(self, entity):
        return self.service.query(entity._entity)
