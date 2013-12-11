from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

from post.api import ArticleList, ArticleDetail

urlpatterns = patterns('',
    #home-page
    url(r'^$', 'post.views.home', name='home'),
    #include admin urls from all the app
    url(r'^admin/', include(admin.site.urls)),
    #fetch all article
    url(r'^articles', ArticleList.as_view(), name='post'),
    #fetch article whose id== pk
    url(r'^article/(?P<pk>[0-9]+)/$', ArticleDetail.as_view()),
    #ckeditor-urls
    (r'^ckeditor/', include('ckeditor.urls')),
    #include social-auth urls for login from google/facebook/git
    url(r'', include('social_auth.urls')),
    #this url is mentioned on google api.
    url(r'^/complete/google-oauth2/$', 'post.views.home', name='home'),
    #to flush out the session
    url(r'^log_out', 'post.views.log_out', name='log_out'),
)

from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns += staticfiles_urlpatterns()