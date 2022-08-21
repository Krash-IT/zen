from fastapi import APIRouter

router = APIRouter(tags=["shops"])


@router.get("/shops")
def list_shops():
    return []
