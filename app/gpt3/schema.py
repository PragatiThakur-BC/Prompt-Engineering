from pydantic import BaseModel
from typing import Optional


class MessageFormat(BaseModel):
    role_1: str = "system"
    content: Optional[str] = "You are a helpful assistant"
    role_2: str = "user"


class Prompt(BaseModel):
    prompt: str


class MessageRequest(BaseModel):
    message_format: MessageFormat
    prompt: Prompt
