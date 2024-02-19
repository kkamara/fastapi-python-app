from typing import Optional
from fastapi import Body, FastAPI, status, HTTPException
from pydantic import BaseModel
from random import randrange

app = FastAPI()

my_posts = [{"title": "Title of Post 1", "content": "Content of post 1.", "id": 1}, {"title": "Favourite Foods", "content": "I like Pizza", "id": 2}]

class Post(BaseModel):
    title: str
    content: str
    published: bool = True
    rating: Optional[int] = None

def find_post(id: int):
    for p in my_posts:
        if p["id"] == id:
            return p

@app.get("/")
def root():
    return {"message": "Hello World"}

@app.get("/posts")
def get_posts():
    return {"data": my_posts}

@app.post("/posts")
def create_posts(post: Post):
    post_dict = post.model_dump()
    post_dict["id"] = randrange(0, 1000000)
    my_posts.append(post_dict)
    return {"data": post_dict}

@app.get("/posts/{id}")
def get_post(id: int):
    post = find_post(id)
    if not post:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"Post with id {id} was not found.")
    return {"post_detail": post}