from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from controllers.translate_controller import router

app = FastAPI()

app.include_router(router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)