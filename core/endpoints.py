from fastapi import APIRouter

router = APIRouter()


@router.get("/test")
def get_test_only():
    return {"message": "test only", "status": "ok"}
