from typing import Optional
from fastapi import FastAPI, Response, status

app = FastAPI()

@app.get("/")
def get_hello() :
    return "Hello~"

# get_blog_id 뒤에 이 함수를 둘 경우 우선순위가 get_blog_id 보다 낮아져서
# get_blog_id 가 먼저 실행된다. 그결과 all 은 int 가 아니므로 이는 url request 에 부합하지 않아서 오류를 발생시킨다.
@app.get('/blog/all',
         tags=['blog'],
         summary="retrive all blogs")
def get_all_blogs(page = 1, page_size: Optional[int] = None) :
    '''
        Summary : this function retirve all blogs
        - **page** : page number (default = 1)
        - **page_size** : Optional query parameter 
    '''
    return {"Message" : f"All {page_size} blogs on page {page}"}

# id 값에 따라서 웹의 status code 를 바꾼다.
@app.get('/blog/{id}', tags=['blog'])
def get_blog_id(id : int, response : Response) :
    if id > 5 :
        response.status_code = status.HTTP_404_NOT_FOUND
        return {"error" : "Not Found"}
    else :
        response.status_code = status.HTTP_200_OK 
        return {"message" : f"id : {id}"} 
    



