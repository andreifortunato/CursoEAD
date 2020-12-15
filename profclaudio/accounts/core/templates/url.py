from django.conf.urls import patterns, include, url

 urlpatterns=patterns('profclaudio.core.views'),
     url(r'^$','home', nome='home'),
     url(r'^contato/$','contact', name='contact'),
                       )