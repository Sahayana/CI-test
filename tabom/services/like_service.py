from tabom.models import Article, Like, User


def do_like(user_id: int, article_id: int) -> Like:
    User.objects.filter(id=user_id).get()
    article = Article.objects.filter(id=article_id).get()

    like = Like.objects.create(user_id=user_id, article_id=article_id)
    article.like_count += 1
    article.save()

    return like


def undo_like(user_id: int, article_id: int) -> None:
    like = Like.objects.filter(user_id=user_id, article_id=article_id).get()
    deleted_cnt, _ = like.delete()  # 'delete' method returns 2 deleted values: the number of rows and data in dict
    if deleted_cnt:
        article = Article.objects.filter(id=article_id).get()
        article.like_count -= 1
        article.save()
