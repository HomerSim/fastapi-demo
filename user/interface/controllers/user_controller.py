from fastapi import APIRouter
from pydantic import BaseModel
from user.application.user_service import UserService

router = APIRouter(prefix="/users")

class CreateUserBody(BaseModel):
    name: str
    email: str
    password: str


@router.post("", status_code=201)
def create_user(user: CreateUserBody):
    user_service = UserService()
    created_user = user_service.create_user(
        name = user.name,
        email = user.email,
        password = user.password
    )

    return created_user

#@router.get("")
# def get_users(user_service: UserService):
#     return user_service.get_users()
"""

curl -X POST 'localhost:8000/users' \
-H 'accept: application/json' \
-H 'Content-Type: application/json' \
-d '{"name": "Dexter3", "email": "test1@naver.com", "password": "1234"}'


curl -X POST -i 'localhost:8000/users' \
-H 'accept: application/json' \
-H 'Content-Type: application/json' \
-d '{"name": "Dexter", "email": "test1@naver.com", "password": 1234}'

"""