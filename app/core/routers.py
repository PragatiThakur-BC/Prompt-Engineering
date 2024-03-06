from fastapi import APIRouter
from app.constants import error_responses
from app.llama70B.endpoint import llama_router
from app.gpt3.endpoint import gpt_router

core_router = APIRouter(prefix="/api",
                        responses=error_responses
                        )
core_router.include_router(llama_router)
core_router.include_router(gpt_router)
