import datetime
from fastapi import FastAPI
from pydantic import BaseModel
from typing import Text

app = FastAPI()

posts = []
#Post DTO
class Post(BaseModel):
    id: str
    title: str
    author: str
    content: Text
    created_at: datetime = datetime.now()
    published_at: datetime
    published : bool = False

@app.get('/')
def read_root():
    return {"welcome": "Welcome to my rest API"}

@app.get('/posts')
def get_posts():
    return posts

@app.post('/posts')
def save_post(post: Post):
    print(post)