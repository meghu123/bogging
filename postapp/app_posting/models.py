from django.contrib.auth.models import User
from django.db import models
from django.contrib.auth.models import User

from . import validation
from django.core.validators import ValidationError
from .validation import PasswordValidator

# Create your models here.
class Tags(models.Model):
    tag_name=models.CharField(max_length=20)

class Post(models.Model):
    Create_by=models.ForeignKey(User,on_delete=models.CASCADE)
    title=models.CharField(max_length=30)
    description=models.TextField(max_length=2000)
    tags=models.ManyToManyField(Tags)

    def __str__(self):
        return f"{self.title}"


class comment(models.Model):
    post=models.ForeignKey(Post,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    content=models.TextField(max_length=120)
    time=models.DateField(auto_now_add=True)

    def __str__(self):
        return "{}{}".format(self.post.title,str(self.user.username))


