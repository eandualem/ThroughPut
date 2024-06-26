from typing import Any, Dict, List
from .weaviate_client import WeaviateClient
from .weaviate_service import WeaviateService


class RouteService(WeaviateService):
    def __init__(self, weaviate_client: WeaviateClient):
        super().__init__(weaviate_client)

    @property
    def object_type(self) -> str:
        return "Route"

    @property
    def properties(self) -> List[str]:
        return ["_additional{id}", "route", "prompt"]

    async def upsert(self, response_data: Dict[str, Any]) -> str:
        return await self.client.create_object(response_data, self.object_type)

    async def batch_upsert(self, response_data: List[Dict[str, Any]]) -> bool:
        return await self.client.batch_create_objects(response_data, self.object_type)

    async def search(self, query: str, fields: List[str], limit: int = 10) -> List[Dict[str, Any]]:
        return await self.client.search(self.object_type, query, fields, limit)
