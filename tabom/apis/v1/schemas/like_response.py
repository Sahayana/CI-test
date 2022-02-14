from ninja import Schema


class LikeResponse(Schema):
    id: int
    user_id: int
    article_id: int

# 스키마에 정의하지 않은 필드 (created_at, updated_at)는 클라이언트에 response로 가지 않는다.