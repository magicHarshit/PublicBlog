from django.contrib.auth.models import User
from django.db import models
from ckeditor.fields import RichTextField

class Article(models.Model):
    user = models.ForeignKey(User)
    title = models.CharField(max_length=300)
    content = RichTextField(config_name='awesome_ckeditor')
    creation_date = models.DateTimeField(auto_now_add=True)
    
    approved = models.BooleanField(default=False)
    view_count = models.PositiveIntegerField(default=0)
    favourite_count = models.PositiveIntegerField(default=0)
    favorited_by = models.ManyToManyField(User, through='FavoriteArticle', related_name='unused_favorite_threads')

    closed = models.BooleanField(default=False)
    closed_by = models.ForeignKey(User, null=True, blank=True) #, related_name='closed_questions')
    closed_at = models.DateTimeField(null=True, blank=True)
    close_reason = models.SmallIntegerField(
                                            choices=const.CLOSE_REASONS,
                                            null=True,
                                            blank=True
                                        )
    deleted = models.BooleanField(default=False, db_index=True)
    points = models.IntegerField(default = 0, db_column='score')

    def __unicode__(self):
        return self.title



class Comment(models.Model):
    user = models.ForeignKey(User)
    post = models.ForeignKey(Article)
    content = models.TextField()
    creation_date = models.DateTimeField(auto_now_add=True)
    def __unicode__(self):
        return self.content

        
class FavoriteArticle(models.Model):
    """A favorite Article of a User."""
    thread = models.ForeignKey(Thread)
    user = models.ForeignKey(User, related_name='user_favorite_article')
    added_at = models.DateTimeField(default=datetime.datetime.now)


    def __str__(self):
        return unicode(self).encode('utf-8')

    def __unicode__(self):
        return u'[%s] favorited at %s' %(self.user, self.added_at)        
