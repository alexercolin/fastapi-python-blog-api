from fastapi import APIRouter, Depends, status, Response, HTTPException
from sqlalchemy.orm import Session
from .. import schemas, database, models
from ..hashing import Hash


def get_all(db: Session = Depends(database.get_db)):
    blogs = db.query(models.Blog).all()
    return blogs

def get_by_id(id: int, response: Response, db: Session = Depends(database.get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Blog with the id {id} is not available')

    return blog

def create(request: schemas.Blog, db: Session = Depends(database.get_db)):
    new_blog = models.Blog(
        title=request.title, body=request.body)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog

def delete(id: int, response: Response, db: Session = Depends(database.get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id)

    if not blog.first():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail='not found')

    blog.delete(synchronize_session=False)
    db.commit()
    return'done'


def updateBlogById(id, request: schemas.Blog, db: Session = Depends(database.get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id)

    if not blog.first():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail='not found')

    blog.update({'title': request.title, 'body': request.body},
                synchronize_session='evaluate')
    db.commit()
    return'done'