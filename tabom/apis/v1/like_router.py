from typing import Tuple
from ninja import Router
from tabom.models import Like, User, Article
from django.http import HttpRequest
from tabom.services.like_service import do_like, undo_like
from tabom.apis.v1.schemas.like_request import LikeRequest
from tabom.apis.v1.schemas.like_response import LikeResponse

router = Router()

@router.post("/", response={201: LikeResponse})
def post_like(request: HttpRequest, like_request: LikeRequest) -> Tuple[int, Like]:
    like = do_like(user_id=LikeRequest.user_id, article_id=LikeRequest.article_id)
    return 201, like

@router.delete("/", response={204: None})
def delete_like(request: HttpRequest, user_id: int, article_id: int) -> Tuple[int, Like]:
    undo_like(user_id=user_id, article_id=article_id)
    return 204, None