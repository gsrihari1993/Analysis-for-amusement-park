from django.conf.urls import url

from . import views
from .views import graph, index, index2,index3, index4, index5,index6
'''
urlpatterns = [
    url(r'^$', views.index, name='index'),
]'''
urlpatterns = [
    url(r'^$', graph),
    url(r'^nu_eda/', index, name='index'),
	url(r'^nu_eda2/', index2, name='index2'),
	url(r'^nu_eda4/', index4, name='index4'),
	url(r'^nu_eda3/', index3, name='index3'),
	url(r'^nu_eda5/', index5, name='index5'),
	url(r'^nu_eda6/', index6, name='index6')
]