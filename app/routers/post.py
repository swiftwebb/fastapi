from fastapi import FastAPI, Response, status, HTTPException, Depends, APIRouter
from sqlalchemy.orm import Session
from typing import List, Optional

from sqlalchemy import func
# from sqlalchemy.sql.functions import func
from .. import models, schemas, oauth2
from ..database import get_db


# router = APIRouter(
#     prefix="/posts",
#     tags=['Posts']
# )


# # @router.get("/", response_model=List[schemas.Post])
# @router.get("/", response_model=List[schemas.PostOut])
# def get_posts(db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user), limit: int = 10, skip: int = 0, search: Optional[str] = ""):
#     # results = db.query(models.Post, func.count(models.Vote.post_id).label("votes")).join(
#     #     models.Vote, models.Vote.post_id == models.Post.id, isouter=True).group_by(models.Post.id)

#     # cursor.execute("""SELECT * FROM posts """)
#     # posts = cursor.fetchall()

#     # posts = db.execute(
#     #     'select posts.*, COUNT(votes.post_id) as votes from posts LEFT JOIN votes ON posts.id=votes.post_id  group by posts.id')
#     # results = []
#     # for post in posts:
#     #     results.append(dict(post))
#     # print(results)
#     # posts = db.query(models.Post).filter(
#     #     models.Post.title.contains(search)).limit(limit).offset(skip).all()

#     posts = db.query(models.Post, func.count(models.Vote.post_id).label("votes")).join(
#         models.Vote, models.Vote.post_id == models.Post.id, isouter=True).group_by(models.Post.id).filter(models.Post.title.contains(search)).limit(limit).offset(skip).all()
#     return posts


# @router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.Post)
# def create_posts(post: schemas.PostCreate, db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):
#     # cursor.execute("""INSERT INTO posts (title, content, published) VALUES (%s, %s, %s) RETURNING * """,
#     #                (post.title, post.content, post.published))
#     # new_post = cursor.fetchone()

#     # conn.commit()

#     new_post = models.Post(owner_id=current_user.id, **post.dict())
#     db.add(new_post)
#     db.commit()
#     db.refresh(new_post)

#     return new_post


# @router.get("/{id}", response_model=schemas.PostOut)
# def get_post(id: int, db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):
#     # cursor.execute("""SELECT * from posts WHERE id = %s """, (str(id),))
#     # post = cursor.fetchone()
#     # post = db.query(models.Post).filter(models.Post.id == id).first()

#     post = db.query(models.Post, func.count(models.Vote.post_id).label("votes")).join(
#         models.Vote, models.Vote.post_id == models.Post.id, isouter=True).group_by(models.Post.id).filter(models.Post.id == id).first()

#     if not post:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
#                             detail=f"post with id: {id} was not found")

#     return post


# @router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
# def delete_post(id: int, db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):

#     # cursor.execute(
#     #     """DELETE FROM posts WHERE id = %s returning *""", (str(id),))
#     # deleted_post = cursor.fetchone()
#     # conn.commit()
#     post_query = db.query(models.Post).filter(models.Post.id == id)

#     post = post_query.first()

#     if post == None:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
#                             detail=f"post with id: {id} does not exist")

#     if post.owner_id != current_user.id:
#         raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
#                             detail="Not authorized to perform requested action")

#     post_query.delete(synchronize_session=False)
#     db.commit()

#     return Response(status_code=status.HTTP_204_NO_CONTENT)


# @router.put("/{id}", response_model=schemas.Post)
# def update_post(id: int, updated_post: schemas.PostCreate, db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):

#     # cursor.execute("""UPDATE posts SET title = %s, content = %s, published = %s WHERE id = %s RETURNING *""",
#     #                (post.title, post.content, post.published, str(id)))

#     # updated_post = cursor.fetchone()
#     # conn.commit()

#     post_query = db.query(models.Post).filter(models.Post.id == id)

#     post = post_query.first()

#     if post == None:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
#                             detail=f"post with id: {id} does not exist")

#     if post.owner_id != current_user.id:
#         raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
#                             detail="Not authorized to perform requested action")

#     post_query.update(updated_post.dict(), synchronize_session=False)

#     db.commit()

#     return post_query.first()








router  = APIRouter(
    prefix="/posts",
    tags = ["Posts"]
)






@router.get("/", response_model= List[schemas.PostOut])
def get_post(db: Session = Depends(get_db), current_user: int=Depends(oauth2.get_current_user),limit: int = 10, skip: int=0, search: Optional[str] = ""):
    # posts = db.query(models.Post).all()


    # posts = db.query(models.Post).filter(models.Post.title.contains(search)).limit(limit).offset(skip).all()

    # posts = db.query(models.Post).filter(models.Post.owner_id ==current_user.id).all()
    posts = db.query(models.Post, func.count(models.Vote.post_id).label("votes")).join(
        models.Vote, models.Vote.post_id == models.Post.id, isouter=True).group_by(models.Post.id).filter(models.Post.title.contains(search)).limit(limit).offset(skip).all()


    return posts 









@router.post("/", status_code=status.HTTP_201_CREATED, response_model= schemas.Post)
def crr(nn: schemas.PostCreate, db: Session = Depends(get_db), current_user: int=Depends(oauth2.get_current_user)):
    print(current_user.email)
    new = models.Post(owner_id = current_user.id,**nn.dict())  # <-- FIXED
    db.add(new)
    db.commit()
    db.refresh(new)
    return  new




@router.get("/{id}", response_model= schemas.PostOut)
def get_post(id:int, db: Session = Depends(get_db), current_user: int=Depends(oauth2.get_current_user)):
    # det = db.query(models.Post).filter(models.Post.id==id).first()
    det = db.query(models.Post, func.count(models.Vote.post_id).label("votes")).join(
        models.Vote, models.Vote.post_id == models.Post.id, isouter=True).group_by(models.Post.id).filter(models.Post.id==id).first()
    if not det:
        raise HTTPException(status_code=404, detail=f"Post with id {id} does not exist")
    # if det.owner_id != current_user.id:
    #     raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail = f"you are not the owner of this post")
    return  det 

@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_p(id: int,  db: Session = Depends(get_db), current_user: int=Depends(oauth2.get_current_user)):
    deleted_post_q = db.query(models.Post).filter(models.Post.id==id)
    deleted_post = deleted_post_q.first()
    if deleted_post is None:
        raise HTTPException(status_code=404, detail=f"Post with id {id} does not exist")
    if deleted_post.owner_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail = f"you are not the owner of this post")
    deleted_post_q.delete(synchronize_session=False)
    db.commit()

    return Response(status_code=status.HTTP_204_NO_CONTENT)

@router.put("/{id}", response_model= schemas.Post)
def update_pppp(id:int, nn:schemas.PostCreate, db: Session = Depends(get_db), current_user: int=Depends(oauth2.get_current_user)):
   update_query = db.query(models.Post).filter(models.Post.id==id)
   post = update_query.first()
   if post.owner_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail = f"you are not the owner of this post")
   ppp = update_query.update(nn.dict(), synchronize_session=False)
   db.commit()
   return  update_query.first() 