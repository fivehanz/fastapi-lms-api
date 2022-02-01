from typing import Optional, List
from fastapi import FastAPI, Path
from pydantic import BaseModel
from api import users, courses, sections

app = FastAPI(
    title="fastapi lms api",
)

app.include_router(users.router)
app.include_router(courses.router)
app.include_router(sections.router)
