from django.contrib.auth.models import User
from django.db import models
from ckeditor.fields import RichTextField

class Article(models.Model):
    user = models.ForeignKey(User)
    title = models.CharField(max_length=300)
    content = RichTextField(config_name='awesome_ckeditor')
    creation_date = models.DateTimeField(auto_now_add=True)
    published = models.BooleanField(default=False)

    def __unicode__(self):
        return self.content



class Comment(models.Model):
    user = models.ForeignKey(User)
    post = models.ForeignKey(Article)
    content = models.TextField()
    creation_date = models.DateTimeField(auto_now_add=True)
    def __unicode__(self):
        return self.content