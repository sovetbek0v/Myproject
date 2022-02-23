from django.contrib.auth import get_user_model
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from post.models import SomePost

User = get_user_model()


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='comment')
    post = models.ForeignKey(SomePost, on_delete=models.CASCADE, related_name='comment')
    comment = models.TextField()
    rating = models.IntegerField(default=5, validators=[MaxValueValidator(5), MinValueValidator(1)], blank=True)

    def __str__(self):
        return f'{self.post.title}'
