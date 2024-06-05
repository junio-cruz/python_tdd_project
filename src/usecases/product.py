from uuid import UUID
from typing import List

import pymongo

from src.infra.db.mongo import db_client
from src.infra.schemas.product import ProductIn, ProductOut
from src.infra.exceptions.exceptions import NotFoundException
from motor.motor_asyncio import AsyncIOMotorClient, AsyncIOMotorDatabase


class ProductUseCase:
    def __init__(self) -> None:
        self.client: AsyncIOMotorClient = db_client.get()
        self.database: AsyncIOMotorDatabase = self.client.get_database()
        self.collection = self.database.get_collection('products')

    async def create(self, body: ProductIn) -> ProductOut:
        product = ProductOut(**body.model_dump())
        await self.collection.insert_one(product.model_dump())
        return product

    async def get(self, id: UUID) -> ProductOut:
        response = await self.collection.find_one({"id": id})

        if not response:
            raise NotFoundException(message=f"PRODUCT_NOT_FOUND: {id}")

        return ProductOut(**response)

    async def list(self) -> List[ProductOut]:
        return [ProductOut(**item) async for item in self.collection.find()]

    async def update(self, id: UUID, body: ProductIn) -> ProductOut:
        response = await self.collection.find_one_and_update(
            filter={"id": id},
            update={"$set": body.model_dump(exclude_none=True)},
            return_document=pymongo.ReturnDocument.AFTER
        )

        return ProductOut(**response)

    async def delete(self, id: UUID) -> ProductOut:
        response = await self.collection.find_one_and_delete({"id": id})
        return ProductOut(**response)


product_use_case = ProductUseCase()
