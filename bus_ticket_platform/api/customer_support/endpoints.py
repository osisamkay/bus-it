# api/customer_support/endpoints.py
from ninja import Router

router = Router()


@router.get("/faq", tags=["Customer Support"])
def faq(request):
    return {"message": "FAQ"}


@router.post("/contact_us", tags=["Customer Support"])
def contact_us(request):
    return {"message": "Contact form submitted"}
