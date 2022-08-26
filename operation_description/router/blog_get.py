from fastapi import APIRouter
from typing import Optional
from fastapi import Response, status

router = APIRouter(
    prefix='/blog',
    tags=['blog']
)

# get_blog_id 뒤에 이 함수를 둘 경우 우선순위가 get_blog_id 보다 낮아져서
# get_blog_id 가 먼저 실행된다. 그결과 all 은 int 가 아니므로 이는 url request 에 부합하지 않아서 오류를 발생시킨다.
@router.get('/all',
         summary="retrive all blogs",
         response_description="This is available blogs")
def get_all_blogs(page = 1, page_size: Optional[int] = None) :
    '''
        Summary : this function retirve all blogs
        - **page** : page number (default = 1)
        - **page_size** : Optional query parameter 
    '''
    return {"Message" : f"All {page_size} blogs on page {page}"}

# id 값에 따라서 웹의 status code 를 바꾼다.
@router.get('/{id}')
def get_blog_id(id : int, response : Response) :
    if id > 5 :
        response.status_code = status.HTTP_404_NOT_FOUND
        return {"error" : "Not Found"}
    else :
        response.status_code = status.HTTP_200_OK 
        return {"message" : f"id : {id}"} 
    
@router.get('/{id}/comments/{comments_id}', tags=['comment'])
def get_comment(id: int, comments_id: int, valid: bool = True, username: Optional[str] = None) :
    return {"message" : f"blog_id {id}, comments_id {comments_id}, valid {valid}, username {username}"}
