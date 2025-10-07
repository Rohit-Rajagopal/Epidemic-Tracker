from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import os
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

db_url = os.environ['DB_URL']
if db_url.startswith("sqlite:///"):
    # Extract the relative path
    relative_path = db_url.replace("sqlite:///", "")

    # Resolve it relative to *this* file’s parent directory (backend/)
    abs_path = Path(__file__).resolve().parent / relative_path

    # Normalize (removes ".." etc.)
    abs_path = abs_path.resolve()

    # Build proper URL
    db_url = f"sqlite:///{abs_path}"

engine = create_engine(db_url, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)
Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()