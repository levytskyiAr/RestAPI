from models.user import User
from sqlalchemy.orm import Session
from dto import user

def create_user(data: user.User, db: Session):
    user = User(**data.model_dump(exclude_unset=True))
    try:
        db.add(user)
        db.commit()
        db.refresh(user)
    except Exception as e:
        print("e")
    return user

def get_user(id: int, db:Session):
    return db.query(User).get(id)

def update_user(data: user.User, db: Session, id: int):
    user = db.query(User).filter(User.id == id).first()
    user.name = data.name
    db.commit()
    db.refresh(user)
    return user

def delete_user(id: int, db: Session):
    user = db.query(User).filter(User.id == id).delete()
    db.commit()
    return user