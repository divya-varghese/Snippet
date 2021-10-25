from django.db import models
from django.utils import timezone

from account.models import User
# Create your models here.


#model for snippet titles
class Tag(models.Model):
    title   =   models.CharField(max_length=150,unique=True)

    def __str__(self):
        return self.title

# model for snippet textes
class Content(models.Model):
    user        =   models.ForeignKey(User,on_delete=models.CASCADE,related_name='user')
    text_title  =   models.ForeignKey(Tag,on_delete=models.CASCADE,related_name='content_title')
    content     =   models.TextField(blank=True,null=False)
    created     =   models.DateTimeField(default=timezone.now)


    def __str__(self):
        return self.text_title.title + ' - ' + self.content[:10]
