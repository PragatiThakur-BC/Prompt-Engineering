from fastapi import FastAPI, status
from app.core.config import settings
from starlette.middleware.cors import CORSMiddleware
from app.core.routers import core_router

app = FastAPI()
if settings.BACKEND_CORS_ORIGINS:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=[str(origin) for origin in settings.BACKEND_CORS_ORIGINS],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )


@app.get("/", status_code=status.HTTP_200_OK)
async def root():
    """
    Health check route
    :return: {"message": "Health Check", "status": True}
    """
    return {"message": "Health Check", "status": True}


app.include_router(core_router)
