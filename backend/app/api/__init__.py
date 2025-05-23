from fastapi import APIRouter
from app.api.routes_chats import router as chat_router
from app.api.routes_matching import router as matching_router
from app.api.routes_tariffs import router as tariffs_router
from app.api.routes_insurers import router as insurers_router
from app.api.routes_ppv import router as ppv_router
from app.api.routes_tariff_features import router as tariff_feature_router
from app.api.routes_tariff_costs import router as tariff_costs_router

router = APIRouter()
router.include_router(chat_router)
router.include_router(matching_router)
router.include_router(tariffs_router)
router.include_router(insurers_router)
router.include_router(ppv_router)
router.include_router(tariff_feature_router)
router.include_router(tariff_costs_router)
