from fastapi import APIRouter
from app.constants import error_responses

llama_router = APIRouter(tags=["Llama-70B"],
                         responses=error_responses
                         )
