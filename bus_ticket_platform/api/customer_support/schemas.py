# api/customer_support/schemas.py
from pydantic import BaseModel


class FAQSchema(BaseModel):
    question: str
    answer: str


class ContactUsSchema(BaseModel):
    name: str
    email: str
    message: str
