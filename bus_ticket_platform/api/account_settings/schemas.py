from pydantic import BaseModel
from typing import Optional


class ProfileSchema(BaseModel):
    user_id: int
    name: str
    email: str
    phone: Optional[str] = None


class NotificationPreferencesSchema(BaseModel):
    user_id: int
    email_notifications: bool
    sms_notifications: bool


class PaymentMethodsSchema(BaseModel):
    user_id: int
    payment_methods: List[str]  # e.g., ["credit_card", "paypal"]
