from fastapi import APIRouter

from api.v1.language import router as language_router


router_v1 = APIRouter()

router_v1.include_router(language_router, prefix='/language', tags=['language'])