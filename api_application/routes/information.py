from fastapi import APIRouter, Depends
from fastapi.security import HTTPBearer
from fastapi_limiter.depends import RateLimiter
from pydantic.class_validators import validator
from pydantic.main import BaseModel
from starlette.requests import Request
from starlette.responses import JSONResponse

formatted_router = APIRouter()
token_auth_scheme = HTTPBearer()


class NumberInformation(BaseModel):
    any_number: int

    @validator('any_number')
    def bigger_than(cls, any_number):
        if any_number < 60:
            raise ValueError('The value should be bigger than 60')
        return any_number


@formatted_router.get('/get_my_token', tags=['Інформація'], dependencies=[Depends(RateLimiter(seconds=1))])
async def get_payout_status_list(request: Request, token: str = Depends(token_auth_scheme)):
    asker_ip = request.client.host
    return JSONResponse(content={'message': 'ok', 'data': token.credentials},
                        media_type="application/json")


@formatted_router.post('/get_half', tags=['Інформація'], dependencies=[Depends(RateLimiter(seconds=1))])
async def receive_callback_secret(payout: NumberInformation, request: Request, token: str = Depends(token_auth_scheme)):
    asker_ip = request.client.host
    return JSONResponse(content={
        'message': 'ok', 'your_token': token.credentials, 'half_of_your_number': payout.any_number / 2},
        media_type="application/json")
