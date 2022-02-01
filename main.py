from typing import Optional, List
from fastapi import FastAPI, Path
from pydantic import BaseModel

app = FastAPI(
    title="fastapi lms",
)


class User(BaseModel):
    email: str
    is_active: bool
    bio: Optional[str]


users = []


@app.get("/users", response_model=List[User])
async def get_users():
    return users


@app.post("/users")
async def create_users(user: User):
    users.append(user)
    return {"message": "Hello, Hanz!"}


@app.get("/users/{id}")
async def get_user(
        id: int = Path(..., description="ID of the user."), 
        
        ):
    return users[id]
