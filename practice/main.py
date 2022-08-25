from fastapi import FastAPI
from typing import Optional
from enum import Enum

app = FastAPI()

@app.get('/')
def index() :
    return "hello world"

# ?로 파라미터 값을 입력 받는다.
@app.get('/blog/all')
def get_all_blogs(page = 1, page_size: Optional[int] = None) :
    return {'message' : f"All {page_size} blogs on page {page}"}

# 주소값으로 파라미터 값을 입력받는다.
@app.get('/blog/{id}/comments/{comment_id}')
def get_comment(id: int, comment_id: int, valid: bool = True, userName: Optional[str] = None) :
    return {'message' : f"blog_id {id} comment_id {comment_id}, valid {valid}, userName {userName}"}

