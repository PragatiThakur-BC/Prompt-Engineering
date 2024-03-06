from app.gpt3.router import gpt_router
from fastapi import status, HTTPException, Response
from app.gpt3.schema import MessageRequest
from app.core.logger_config import api_logger
from app.gpt3 import services
from starlette.responses import JSONResponse


@gpt_router.post("/messages/get-response-gpt", status_code=status.HTTP_200_OK)
async def get_response(request: MessageRequest, frequency_penalty: float = 1, presence_penalty: float = 1,
                       top_p: float = 0.7, n: int = 10, temperature: float = 0.7):
    """
    Endpoint to get response from AI model
    :param request: Question/prompt to AI model
    :param frequency_penalty: penalty from repeating the same tokens
    :param presence_penalty:
    :param top_p: considers tokens whose cumulative probability mass is less than this value.
    :param n: number of completions to generate.(how many alternative code completions will be returned by the model)
    :param temperature: randomness of token generation
    :return: {"status": True, "response": response}
    """
    try:
        messages = services.create_message(request)
        if not messages:
            raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail="PLease Provide a prompt to "
                                                                                         "continue.")
        response = services.get_code_completion(messages, frequency_penalty, presence_penalty, top_p, n,
                                                temperature)
        if not response:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Could not generate, Try "
                                                                                          "again "
                                                                                          "or contact support for "
                                                                                          "assistance.")
        api_logger.info("Successfully generated response for the prompt!")
        return response
    except HTTPException as he:
        api_logger.info(f"{he.detail}")
        return JSONResponse({"status": False, "message": he.detail},
                            status_code=he.status_code)
    except Exception as err:
        api_logger.error(f"An unexpected error occurred, {err}")
        return JSONResponse({"status": False, "message": "Unexpected error occurred please try again"},
                            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)
