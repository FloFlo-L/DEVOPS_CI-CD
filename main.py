from fastapi import FastAPI
from controllers.translate_controller import router

app = FastAPI()

app.include_router(router)
