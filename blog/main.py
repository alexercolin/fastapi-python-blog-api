from fastapi import FastAPI
from .core.models import models
from .db import database
from .routers import blog, users, authentication

app = FastAPI()

engine = database.engine

models.Base.metadata.create_all(engine)

app.include_router(authentication.router)
app.include_router(blog.router)
app.include_router(users.router)
