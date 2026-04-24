from fastapi import FastAPI

app = FastAPI()

from app.routes.ai_routes import ai_router

app.include_router(ai_router)