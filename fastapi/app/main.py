from fastapi import APIRouter, FastAPI

from .middlwares import DBSessionMiddleware, HttpRequestMiddleware
from .routers.v1 import api_v1_router

app = FastAPI()
app.add_middleware(DBSessionMiddleware)
app.add_middleware(HttpRequestMiddleware)

router = APIRouter()
router.include_router(api_v1_router, prefix="/api/v1", tags=["api/v1"])
app.include_router(router)
