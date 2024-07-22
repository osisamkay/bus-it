from pydantic import BaseModel
from typing import List


class DiscountSchema(BaseModel):
    discount_code: str
    description: str
    amount: float  # discount amount


class PackageDealSchema(BaseModel):
    package_id: int
    description: str
    price: float


class DealsSchema(BaseModel):
    discounts: List[DiscountSchema]
    package_deals: List[PackageDealSchema]
