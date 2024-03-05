import openai
from app.core.config import settings
from app.core.logger_config import script_logger


client = openai.OpenAI(
    api_key=settings.TOGETHER_API_KEY,
    base_url=settings.BASE_URL,
)


def create_message(message_data):
    messages = [
        {
            "role": message_data.role_1,
            "content": message_data.content_1,
        },
        {
            "role": message_data.role_2,
            "content": message_data.prompt,
        }
    ]
    return messages


def get_code_completion(messages, frequency_penalty: float, presence_penalty: float, top_p: float, n: int,
                        temperature: float, max_tokens=settings.MAX_TOKENS, model=settings.MODEL):
    chat_completion = client.chat.completions.create(
        messages=messages,
        model=model,
        max_tokens=max_tokens,
        stop=[
            "<step>"
        ],
        frequency_penalty=frequency_penalty,
        presence_penalty=presence_penalty,
        top_p=top_p,
        n=n,
        temperature=temperature,
    )

    return chat_completion.choices[0].message.content
