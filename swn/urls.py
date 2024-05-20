from django.conf.urls import patterns, url

from swn import views

urlpatterns = patterns('',
    # ex: /swn/                       
    url(r'^$', views.index, name='index'),
    # ex: /swn/5
    url(r'^(?P<swn_id>\d+)/$', views.detail, name='detail'),
    url(r'^(?P<swn_id>\d+)_vote/$', views.voteswn, name='detail'),
    url(r'^(?P<swn_id>\d+)_submit/$', views.addswn, name='detail'),
)
