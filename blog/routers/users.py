from fastapi import APIRouter, Depends, status, Response, HTTPException
from .. import schemas, database, models
from typing import List
from sqlalchemy.orm import Session
from ..repository import users


router = APIRouter(
    prefix='/user',
    tags=['Users']

)

@router.get('/', response_model=List[schemas.Users])
def get_all(db: Session = Depends(database.get_db)):
    return users.get_all(db)

@router.get('/{id}', status_code=status.HTTP_200_OK, response_model=schemas.Users)
def get_by_id(id: int, db: Session = Depends(database.get_db)):
    return users.get_by_id(id,db)


@router.post('/', status_code=status.HTTP_201_CREATED)
def create(request: schemas.User, db: Session = Depends(database.get_db)):
    return users.create(request, db)


@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def delete(id: int, response: Response, db: Session = Depends(database.get_db)):
    return users.delete(id, response, db)