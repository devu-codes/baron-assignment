from fastapi import APIRouter, HTTPException
from sqlmodel import Session, select

from model import User, UserCreate
from database import engine

router = APIRouter()

@router.post("/signup")
def signup(user: UserCreate):
    if not user.username or not user.username.strip():
        raise HTTPException(status_code=400, detail="Username cannot be blank")
    if not user.password or not user.password.strip():
        raise HTTPException(status_code=400, detail="Password cannot be blank")
    if len(user.password) <= 5:
        raise HTTPException(status_code=400, detail="Password must be longer than 5 characters")
    with Session(engine) as session:
        existing_user = session.exec(select(User).where(User.username == user.username)).first()
        if existing_user:
            raise HTTPException(status_code=400, detail="Username already taken.")

        new_user = User(username=user.username, password=user.password)
        session.add(new_user)
        session.commit()
        session.refresh(new_user)
        return {"message": "User signed up successfully", "user_id": new_user.id}

@router.post("/login")
def login(user: UserCreate):
    with Session(engine) as session:
        db_user = session.exec(select(User).where(User.username == user.username)).first()
        if not db_user or db_user.password != user.password:
            raise HTTPException(status_code=401, detail="Invalid username or password")
        return {"message": "Login successful"}
