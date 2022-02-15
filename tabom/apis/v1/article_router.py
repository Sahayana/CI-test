from typing import List, Tuple

from ninja import Router
from tabom.services.article_service import create_an_article, get_an_article, get_article_list, delete_an_article
from tabom.models import Article
from tabom.apis.v1.schemas.article_create_request import ArticleCreateRequest
from tabom.apis.v1.schemas.article_response import ArticleResponse
from django.http import HttpRequest
from django.db.models import QuerySet



router = Router()



@router.post('/', response={201: ArticleResponse})
def create_article(request: HttpRequest, article_create_request: ArticleCreateRequest) -> Tuple(int, Article):
    article = create_article(article_create_request.title)
    return 201, article

# The status code 200 would be returned when an api gets response that does not need to sepecify.
@router.get('/', response=List[ArticleResponse])
def get_articles(request: HttpRequest, user_id:int, offset:int=0, limit:int=10) -> QuerySet[Article]:
    articles = get_article_list(user_id, offset, limit)
    return articles


@router.get('/{article_id}', response=ArticleResponse)
def get_article(request:HttpRequest, user_id:int, article_id:int) -> Article:
    article = get_an_article(user_id, article_id)
    return article

@router.delete('/{article_id}', response={204: None})
def delete_article(request:HttpRequest, article_id:int) -> Tuple[int, None]:
    delete_an_article(article_id)
    return 204, None