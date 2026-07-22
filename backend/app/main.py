"""
Purpose:
Main entry point for the MindRankAI backend application.

Used By:
Uvicorn server.

Edit Carefully:
This file starts the entire backend application.
"""

from fastapi import FastAPI
from app.core.settings import settings

app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
)


@app.get("/")
def root():
    return {
        "app_name": settings.APP_NAME,
        "version": settings.APP_VERSION,
        "debug": settings.DEBUG,
        "message": "Welcome to MindRankAI API 🚀"
    }