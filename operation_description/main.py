from fastapi import FastAPI
from router import blog_get

app = FastAPI()
app.include_router(blog_get.router)

@app.get("/")
def get_hello() :
    return "Hello~"
