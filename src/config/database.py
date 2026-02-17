from sqlmodel import SQLModel, create_engine
from dotenv import load_dotenv
import os

load_dotenv()
DATABASE_URL = os.getenv("DATABASE_URL")

engine = create_engine(DATABASE_URL, echo=True)

def start_database():
    try:
        print("CONNECTING TO DATABASE...")
        SQLModel.metadata.create_all(engine)
        print("DATABASE CONNECTED SUCCESSFULLY")
    except Exception as e:
        print("ERROR DURING DATABASE CONNECTION: \n", e)