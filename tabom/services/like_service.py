from tabom.models import Article, Like, User
from django.db.models import F
from django.db import transaction

@transaction.atomic # tansaction.atomic을 설정한 함수 내부의 DB연산은 atomicity를 보장
def do_like(user_id: int, article_id: int) -> Like:
    User.objects.filter(id=user_id).get()
    Article.objects.filter(id=article_id).get()

    
    '''
    장고의 F expression으로 쿼리 업데이트를 sql 자체에서 실행하도록 설정하여 동시성 해결
    '''
    Article.objects.filter(id=article_id).update(like_count=F('like_count') + 1)
    '''
    서버에서 like_count를 읽고 1씩 업데이트 하면 동시성 해결 불가
    '''
    # article.like_count += 1
    # article.save()
    '''
    DEADLOCK 해결하기 위해 위에서 update를 먼저 하고 create를 나중에 실행
    '''
    like = Like.objects.create(user_id=user_id, article_id=article_id)

    return like


def undo_like(user_id: int, article_id: int) -> None:
    like = Like.objects.filter(user_id=user_id, article_id=article_id).get()
    deleted_cnt, _ = like.delete()  # 'delete' method returns 2 deleted values: the number of rows and data in dict
    if deleted_cnt:
        Article.objects.filter(id=article_id).update(like_count=F("like_count") - 1)
        # article = Article.objects.filter(id=article_id).get()
        # article.like_count -= 1
        # article.save()
