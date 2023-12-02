from fastapi import FastAPI
import uvicorn
import dotenv
import os
from database.connection import db

dotenv.load_dotenv()

print(os.environ.get("DB_URI", ""))
app = FastAPI()

@app.get("/")
def hello():
    return "hello"

@app.get("/test")
def test():
    
    return None
    

if __name__ == "__main__":
    uvicorn.run(app=app, host="0.0.0.0", port=8000)