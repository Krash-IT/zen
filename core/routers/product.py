from fastapi import APIRouter

router = APIRouter(tags=["products"])


@router.get("/products")
def list_product():
    return []
