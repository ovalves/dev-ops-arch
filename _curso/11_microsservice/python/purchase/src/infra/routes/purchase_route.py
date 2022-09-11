from fastapi import APIRouter, HTTPException

router = APIRouter()

@router.post("/purchases", status_code=200)
def get_ticket():
    return {"tickets": []}