from core.db import Base


def get_db():
    db = Base.SessionLocal()
    try:
        yield db
    finally:
        db.close()
