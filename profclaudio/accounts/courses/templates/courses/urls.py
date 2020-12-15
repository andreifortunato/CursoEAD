from django.conf.urls import patterns, include, url

urlpatterns = patterns('profclaudio.courses.views'),
     url(r'^$','index', nome='index'),
)