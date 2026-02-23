import os
from dotenv import load_dotenv
load_dotenv()

# Step 1: create a local session object
from sqlalchemy.orm import sessionmaker, DeclarativeBase
from sqlalchemy import create_engine

# 2) Creating a link to my physical db
DATABASE_URL = os.getenv("DATABASE_URL")

# 3) Engine
engine = create_engine(DATABASE_URL)


# 4) Base class for models
class Base(DeclarativeBase):
    pass

# 5) Session Factory
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)


