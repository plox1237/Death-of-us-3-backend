import os
import uvicorn
from dotenv import load_dotenv
from app import app

load_dotenv()

if __name__ == "__main__":
    port = int(os.getenv("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)