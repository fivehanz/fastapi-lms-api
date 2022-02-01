from typing import Optional, List
from pydantic import BaseModel
import fastapi

router = fastapi.APIRouter()


class User(BaseModel):
    email: str
    is_active: bool
    bio: Optional[str]


users = []


@router.get("/users", response_model=List[User])
async def get_users():
    return users


@router.post("/users")
async def create_users(user: User):
    users.append(user)
    return {"message": "Hello, Hanz!"}


@router.get("/users/{id}")
async def get_user(user_id: int):
    return users[user_id]
