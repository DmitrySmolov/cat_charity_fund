from fastapi import APIRouter

from app.api.endpoints import charityproject_router, user_router
from app.core.config import Constant

main_router = APIRouter()

main_router.include_router(
    router=charityproject_router,
    prefix=Constant.CHARITY_ENDPOINTS_PREFIX,
    tags=Constant.CHARITY_ENDPOINTS_TAGS
)
main_router.include_router(user_router)
