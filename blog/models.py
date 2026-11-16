from django.contrib.auth.models import User
from django.db import models

class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, default=1)
    username = models.CharField(max_length=100)
    # email = models.EmailField(max_length=100)
    # password = models.CharField(max_length=100)
    # registered_on = models.DateTimeField(auto_now_add=True)
    # status = models.BooleanField(default=False, choices=())
    # type = models.BooleanField(max_length=100, choices=())

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=False,
                                 choices=[(True, 'Published'), (False, 'Draft')]
                                 )

class Comment(models.Model):

    status = models.CharField(max_length=1,
                              choices=(("C", "Confirmed"), ("N", "Not Confirmed"), ("D", "Draft")),
                              )
    # status = models.IntegerField(max_length=1,
    #                           choices=[(1, "Confirmed"), (2, "Not Confirmed"), (3, "Draft")],
    #                           )