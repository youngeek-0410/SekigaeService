from app.models import User
from database import SessionLocal

db = SessionLocal()


def seed_user():
    user = User(username="test1", email="test1@example.com", uid="xxxxxxxxxxxxxxxxxx")
    db.add(user)
    db.commit()


if __name__ == "__main__":
    print("Seeding data...")
    seed_user()
