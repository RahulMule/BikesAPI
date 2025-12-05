from fastapi import FastAPI
from .router.game import gamesrouter
app =FastAPI()
app.include_router(gamesrouter)