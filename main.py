from typing import Optional
from fastapi import Body, FastAPI
from pydantic import BaseModel

app = FastAPI()

my_posts = [{"title": "Title of Post 1", "content": "Content of post 1.", "id": 1}, {"title": "Favourite Foods", "content": "I like Pizza", "id": 2}]

class Post(BaseModel):
    title: str
    content: str
    published: bool = True
    rating: Optional[int] = None

@app.get("/")
def root():
    return {"message": "Hello World"}

@app.get("/posts")
def get_posts():
    return {"data": my_posts}

@app.post("/posts")
def create_posts(post: Post):
    print(post)
    print(post.model_dump()) # .dict() is deprecated
    return {"data": "new post"}
