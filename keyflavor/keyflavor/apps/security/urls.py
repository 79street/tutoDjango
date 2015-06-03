__author__ = 'mrx'
from django.conf.urls import patterns, url

urlpatterns = patterns('keyflavor.apps.security.views',
	url(r'^$', 'index_view', name="index"),
	)