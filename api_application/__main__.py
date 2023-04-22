import uvicorn
from fastapi import Request
from fastapi_limiter import FastAPILimiter
from starlette.responses import JSONResponse
import aioredis
from api_application import config
from api_application.misc import app


@app.on_event("startup")
async def startup():
    redis = aioredis.from_url("redis://localhost", encoding="utf-8", decode_responses=True)
    await FastAPILimiter.init(redis)


@app.exception_handler(FileNotFoundError)
async def unicorn_exception_handler(request: Request, exc: FileNotFoundError):
    return JSONResponse(
        status_code=404,
        content={"message": str(exc)},
    )

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=config.api_port)
