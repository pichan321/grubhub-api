from fastapi import FastAPI
import uvicorn
import dotenv
import os
from database.connection import db
from tables.models import *

from fastapi.middleware.cors import CORSMiddleware

dotenv.load_dotenv()

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], #accepts requests from any origin(s)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/restaurants")
def get_restaurants():
    return db.query(Restaurants).limit(20).all()

if __name__ == "__main__":
    uvicorn.run(app=app, host="0.0.0.0", port=8000)