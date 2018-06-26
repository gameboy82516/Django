from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(blank=True)
    photo = models.URLField(blank=True)
    location = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
'''

class Staff(models.Model):
    LoginID = models.CharField(max_length=20)
    Name = models.CharField(max_length=10)
    Sex = models.BooleanField(default=True)
    Birthday = models.CharField(max_length=20, null=True)
    JoinTime = models.DateTimeField()

'''
