from fastapi import FastAPI, status, Response, HTTPException, Depends
from fastapi.params import Body
from pydantic import BaseModel
from typing import Optional,List
import psycopg2
from psycopg2.extras import RealDictCursor
import time
from . import models, schemas, utils
from .database import engine, SessionLocal, get_db
from sqlalchemy.orm import Session
from .routers import post, user, auth, vote
from fastapi.middleware.cors import CORSMiddleware
# models.Base.metadata.create_all(bind=engine)

app = FastAPI()
origins =["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"message": "Hello World m "}


# @app.get("/posts", response_model= List[schemas.Post])
# def get_post(db: Session = Depends(get_db)):
#     posts = db.query(models.Post).all()
#     return posts 









# @app.post("/posts", status_code=status.HTTP_201_CREATED, response_model= schemas.Post)
# def crr(nn: schemas.PostCreate, db: Session = Depends(get_db)):
#     print(nn.dict())
#     new = models.Post(**nn.dict())  # <-- FIXED
#     db.add(new)
#     db.commit()
#     db.refresh(new)
#     return  new




# @app.get("/posts/{id}", response_model= schemas.Post)
# def get_post(id:int, db: Session = Depends(get_db)):
#     det = db.query(models.Post).filter(models.Post.id==id).first()
#     return  det 

# @app.delete("/posts/{id}", status_code=status.HTTP_204_NO_CONTENT)
# def delete_p(id: int,  db: Session = Depends(get_db)):
#     deleted_post = db.query(models.Post).filter(models.Post.id==id)

#     if deleted_post.first() is None:
#         raise HTTPException(status_code=404, detail=f"Post with id {id} does not exist")
#     deleted_post.delete(synchronize_session=False)
#     db.commit()

#     return Response(status_code=status.HTTP_204_NO_CONTENT)

# @app.put("/posts/{id}", response_model= schemas.Post)
# def update_pppp(id:int, nn:schemas.PostCreate, db: Session = Depends(get_db)):
#    update_query = db.query(models.Post).filter(models.Post.id==id)
#    post = update_query.first()
#    ppp = update_query.update(nn.dict(), synchronize_session=False)
#    db.commit()
#    return  update_query.first() 


# @app.post("/users", status_code=status.HTTP_201_CREATED, response_model=schemas.UserOut)
# def create_users(user: schemas.UserCreate, db: Session = Depends(get_db)):
#     print(user.dict())
#     hhh = utils.hash(user.password)
#     user.password = hhh
#     new_user = models.User(**user.dict())  # <-- FIXED
#     db.add(new_user)
#     db.commit()
#     db.refresh(new_user)
#     return  new_user


# @app.get("/users/{id}", response_model=schemas.UserOut)
# def get_post(id:int, db: Session = Depends(get_db)):
#     det = db.query(models.User).filter(models.User.id==id).first()
#     return  det 


# @app.get("/")
# def root():
#     return {"message": "Hello World 221"}
# while True:
#     try:
#         conn = psycopg2.connect(host='localhost',database = 'fastapi',user = 'postgres',password = '1234', cursor_factory=RealDictCursor)
#         cursor = conn.cursor()
#         print("success")
#         break
#     except Exception as error:
#         print("failed", error)
#         time.sleep(10)

# my_post = [{"title":"title of post one","content":"content of post one","id":1},{"title":"title of post two","content":"content of post two","id":2}]

# @app.get("/posts")
# def get_post():
#     cursor.execute("""SELECT * FROM posts""")
#     posts = cursor.fetchall()
#     return{"data": posts}

# @app.post("/posts", status_code=status.HTTP_201_CREATED)
# def crr(nn:Post):
#     cursor.execute("""INSERT INTO posts (title, content, published) VALUES (%s, %s,%s) RETURNING * """, (nn.title, nn.content, nn.published))
#     new_post = cursor.fetchone()
#     conn.commit()
#     return {"data": new_post}

# @app.get("/posts/{id}")
# def get_post(id:int):
#     cursor.execute("""SELECT * FROM posts WHERE id = %s """, (str(id),))
#     test_p = cursor.fetchone()
#     print(test_p)
#     return{"data": test_p}


# @app.delete("/posts/{id}", status_code=status.HTTP_204_NO_CONTENT)
# def delete_p(id: int):
#     cursor.execute("""DELETE FROM posts WHERE id = %s RETURNING * """, (str(id),))
#     deleted_post = cursor.fetchone()
#     conn.commit()

#     if deleted_post is None:
#         raise HTTPException(status_code=404, detail=f"Post with id {id} does not exist")

#     return Response(status_code=status.HTTP_204_NO_CONTENT)



# @app.put("/posts/{id}")
# def update(id:int, nn:Post):
#     cursor.execute("""UPDATE posts SET title= %s, content =%s, published= %s WHERE id=%s RETURNING *""", (nn.title, nn.content, nn.published, str(id)))
#     up = cursor.fetchone()
#     conn.commit()


# @app.post("/create")
# def crr(payload: dict=Body(...)):
#     print(payload)
#     return {"message": "success 221"}

app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(vote.router)


