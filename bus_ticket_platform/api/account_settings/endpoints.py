# api/account_settings/endpoints.py
from ninja import Router

router = Router()


@router.get("/profile", tags=["Account Settings"])
def profile(request):
    return {"message": "User profile"}


@router.post("/notification_preferences", tags=["Account Settings"])
def notification_preferences(request):
    return {"message": "Notification preferences updated"}


@router.post("/payment_methods", tags=["Account Settings"])
def payment_methods(request):
    return {"message": "Payment methods updated"}
