from fastapi import APIRouter
from app.constants import error_responses

gpt_router = APIRouter(tags=["GPT-3.5"],
                       responses=error_responses
                       )
