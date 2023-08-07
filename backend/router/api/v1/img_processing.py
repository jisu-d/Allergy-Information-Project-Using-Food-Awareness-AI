from fastapi import APIRouter
from model.img_processing import CheckFood

router = APIRouter(
    prefix="/api/v1",
)

@router.post("/checkfood")
async def postCheckFood(checkfood: CheckFood):
    return checkfood