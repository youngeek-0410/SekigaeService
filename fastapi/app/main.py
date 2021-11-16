from app.routers.user import router as user_router

from fastapi import APIRouter, FastAPI

router = APIRouter()
router.include_router(user_router, prefix="/users", tags=["users"])

app = FastAPI()
app.include_router(router)
