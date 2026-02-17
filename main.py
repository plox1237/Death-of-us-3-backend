import uvicorn
from app import app
from src.config.database import start_database

if __name__ == "__main__":
    start_database()
    uvicorn.run(app, host="0.0.0.0", port=4000) # uvicorn main:app --host 0.0.0.0 --port 4000