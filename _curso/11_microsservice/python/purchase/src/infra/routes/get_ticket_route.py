from fastapi import APIRouter, HTTPException

router = APIRouter()

@router.get("/tickets/:code", status_code=200)
def get_ticket():
    return {"tickets": []}