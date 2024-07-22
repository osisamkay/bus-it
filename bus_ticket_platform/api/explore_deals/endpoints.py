# api/explore_deals/endpoints.py
from ninja import Router

router = Router()


@router.get("/discounts", tags=["Explore Deals"])
def discounts(request):
    return {"message": "List of discounts"}


@router.get("/package_deals", tags=["Explore Deals"])
def package_deals(request):
    return {"message": "List of package deals"}
