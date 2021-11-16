from app.models import User
from database import local_session

db = local_session()


def seed_user():
    user1 = User(username="test1", email="test1@example.com", uid="xxxxxxxxxxxxxxxxxx")
    user2 = User(username="test2", email="test2@example.com", uid="yyyyyyyyyyyyyyyyyy")
    db.add(user1)
    db.add(user2)
    db.commit()


if __name__ == "__main__":
    print("Seeding data...")
    seed_user()
