from pydantic import BaseModel
from typing import List


class ReceiptItem(BaseModel):
    shortDescription: str
    price: str

class Receipt(BaseModel):
    retailer: str
    purchaseDate: str
    purchaseTime: str
    items: List[ReceiptItem]
    total: str