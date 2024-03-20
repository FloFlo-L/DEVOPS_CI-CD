from fastapi import FastAPI
from controllers.translate_controller import translate_router

app = FastAPI()

app.include_router(translate_router)