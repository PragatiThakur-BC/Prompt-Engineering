from pydantic import BaseModel
from typing import Optional


class SystemMessage(BaseModel):
    role_1: str = "system"
    content_1: Optional[str] = "You are a helpful assistant"


class UserMessage(SystemMessage):
    role_2: str = "user"
    prompt: str

