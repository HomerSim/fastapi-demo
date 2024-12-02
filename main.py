from fastapi import FastAPI
from user.interface.controllers.user_controller import router as user_router

from fastapi.exceptions import RequestValidationError
from fastapi.requests import Request
from fastapi.responses import JSONResponse

app = FastAPI()
app.include_router(user_router)

@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    return JSONResponse(
        status_code=400,
        content=exc.errors(),
    )

@app.get("/")
def hello():
    return {"message": "Hello World"}