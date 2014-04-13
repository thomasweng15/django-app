from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

from polls import views

urlpatterns = patterns('',
	url(r'^polls/', include('polls.urls', namespace="polls")),
	url(r'admin/', include(admin.site.urls)),
	url(r'^$', views.IndexView.as_view(), name='index'),
	url(r'^(?P<pk>\d+)/$', views.DetailView.as_view(), name='detail'),
	url(r'^(?P<pk>\d+)/results/$', views.ResultsView.as_view(), name='results'),
	url(r'^(?P<poll_id>\d+)/vote/$', views.vote, name='vote'),
)