from fastapi import APIRouter, HTTPException

router = APIRouter()

@router.get("/health/")
def health():
    return {"message": "The satus of the app is up!!"}
