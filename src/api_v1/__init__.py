from fastapi import APIRouter

from .creature.views import router as creature_router

router = APIRouter()
router.include_router(router=creature_router, prefix="/creature")