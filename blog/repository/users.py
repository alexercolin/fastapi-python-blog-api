from fastapi import APIRouter, Depends, status, Response, HTTPException
from ..core.models import  models
from ..core.schemas import schemas
from typing import List
from ..db import database
from sqlalchemy.orm import Session
from ..repository import users
from ..auth import hashing

Hash = hashing.Hash


def get_all(db: Session = Depends(database.get_db)):
    users = db.query(models.User).all()
    return users

def get_by_id(id: int, db: Session = Depends(database.get_db)):
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'User with the id {id} is not available')
    return user


def create(request: schemas.User, db: Session = Depends(database.get_db)):
    new_user = models.User(
        name=request.name, email=request.email, password=Hash.bcrypt(request.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


def delete(id: int, response: Response, db: Session = Depends(database.get_db)):
    user = db.query(models.User).filter(models.User.id == id)

    if not user.first():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail='not found')

    user.delete(synchronize_session=False)
    db.commit()
    return'done'