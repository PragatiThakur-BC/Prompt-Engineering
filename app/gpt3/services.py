import openai
from app.core.config import settings
from app.core.logger_config import script_logger
from fastapi import HTTPException
import json

openai.api_key = settings.GPT_API_KEY


def create_message(message_data):
    messages = [
        {
            "role": message_data.message_format.role_1,
            "content": message_data.message_format.content,
        },
        {
            "role": message_data.message_format.role_2,
            "content": message_data.prompt.prompt,
        }
    ]
    return messages


def get_code_completion(messages, frequency_penalty: float, presence_penalty: float, top_p: float, n: int,
                        temperature: float, max_tokens=settings.MAX_TOKENS, model=settings.GPT_MODEL):
    try:
        chat_completion = openai.chat.completions.create(
            messages=messages,
            model=model,
            max_tokens=max_tokens,
            stop=None,
            frequency_penalty=frequency_penalty,
            presence_penalty=presence_penalty,
            top_p=top_p,
            n=n,
            temperature=temperature,
        )
        return chat_completion.choices[0].message.content
    except Exception as e:
        script_logger.error(f"error: {e}")
        raise HTTPException(status_code=500, detail=str(e))
