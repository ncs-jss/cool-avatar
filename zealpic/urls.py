from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^avatar/', 'zealpic.views.home', name='home'),
)
