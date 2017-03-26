from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
	url(r'^$', 'zealpic.views.zealicon', name='zealicon'),
    url(r'^avatar/$', 'zealpic.views.home', name='home'),
)
