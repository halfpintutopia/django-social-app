# from django.db import models
from django.conf import settings
from django.db import models


# class ExampleModel(models.Model):
#     name = models.CharField(
#         verbose_name='name',
#         max_length=100,
#     )
#     text = models.TextField(
#         verbose_name='text',
#         blank=True,
#     )


class Post(models.Model):
    user = models.ForeignKey(
        verbose_name='user',
        to=settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    post = models.TextField(
        verbose_name='post',
    )
    created = models.DateTimeField(
        verbose_name='posted',
        auto_now_add=True,
    )

    def __str__(self):
        return self.post
