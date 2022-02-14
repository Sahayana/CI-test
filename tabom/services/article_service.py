from django.core.paginator import Page, Paginator
from django.db.models import QuerySet, Prefetch

from tabom.models import Article
from tabom.models.like import Like
from tabom.models.user import User
from tabom.services.article_service import *
from tabom.services.like_service import *



def get_an_article(article_id: int) -> Article:
    return Article.objects.filter(id=article_id).get()


# def get_article_list(offset: int, limit: int) -> QuerySet[Article]:  # QuerySet which has Article objects as a member variable.
#     return Article.objects.order_by("-id").prefetch_related("like_set")[offset : offset + limit]


# def get_article_page(page: int, limit: int) -> Page:
#     return Paginator(Article.objects.order_by("-id"), limit).page(page)


def get_article_list(user_id: int, offset: int, limit: int) -> QuerySet[Article]:
    return (
        Article.objects.order_by("-id")
        .prefetch_related("like_set")
        .prefetch_related(Prefetch("like_set", queryset=Like.objects.filter(user_id=user_id), to_attr="my_likes"))[
            offset : offset + limit
        ]
    )