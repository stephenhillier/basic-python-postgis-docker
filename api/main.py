"""
Main application entrypoint that initializes FastAPI
"""
from fastapi import FastAPI, HTTPException
from starlette.middleware.cors import CORSMiddleware

from app.config import DATABASE_URI

app = FastAPI(title="Basic")

# CORS
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get('/api/v1/hello')
def hello_world():
    """ function goes here """
    return "hello"
