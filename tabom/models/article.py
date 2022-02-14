from typing import List, Any
from django.db import models

from tabom.models.base_model import BaseModel


class Article(BaseModel):
    title = models.CharField(max_length=255)

    my_likes: List[Any] # This attr needs to be defined for 'Mypy' operations.