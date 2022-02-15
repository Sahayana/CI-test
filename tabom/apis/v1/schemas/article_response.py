
from typing import Optional, List
from ninja import Schema
from tabom.apis.v1.schemas.like_response import LikeResponse

class ArticleResponse(Schema):
    id: int
    title: str
    my_likes: Optional[List[LikeResponse]]  # Optional: field values can be None.