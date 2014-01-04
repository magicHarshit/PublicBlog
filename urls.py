from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

from post.api import ArticleList, ArticleDetail, TagDetail, TagList, UserList, UserDetail, CommentList, CommentDetail, VoteList, VoteDetail

urlpatterns = patterns('',
    #home-page
    url(r'^$', 'post.views.home', name='home'),
    #include admin urls from all the app
    url(r'^admin/', include(admin.site.urls)),
    #fetch all article
    url(r'^api/articles/$', ArticleList.as_view(), name='post'),
    #fetch article whose id== pk
    url(r'^api/articles/(?P<pk>[0-9]+)/$', ArticleDetail.as_view()),
    #fetch all tags
    url(r'^api/tags/$', TagList.as_view()),
    #fetch tag whose id==pk
    url(r'^api/tags/(?P<pk>[0-9]+)/$', TagDetail.as_view()),

    #fetch all users
    url(r'^api/users/$', UserList.as_view()),
    #fetch user whose id==pk
    url(r'^api/users/(?P<pk>[0-9]+)/$', UserDetail.as_view()),
    #fetch comments of a article.
    url(r'^api/article/(?P<article_id>[0-9]+)/comments/$', CommentList.as_view()),

    url(r'^api/comment/(?P<pk>[0-9]+)/$', CommentDetail.as_view()),

    #ckeditor-urls
    (r'^ckeditor/', include('ckeditor.urls')),
    #include social-auth urls for login from google/facebook/git
    url(r'', include('social_auth.urls')),
    #this url is mentioned on google api.
    url(r'^/complete/google-oauth2/$', 'post.views.home', name='home'),
    #to flush out the session
    url(r'^log_out', 'post.views.log_out', name='log_out'),

    url(r'^get_user', 'post.views.get_user'),

    url(r'^api/vote/$', VoteList.as_view()),

    url(r'^api/vote/(?P<pk>[0-9]+)/$', VoteDetail.as_view()),

)

from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns += staticfiles_urlpatterns()