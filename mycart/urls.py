from django.conf.urls import url
from . import views

app_name = 'mycart'

urlpatterns = [url(r'^$', views.mycart_detail, name='mycart_detail'),
               url(r'^add/(?P<product_id>\d+)/$', views.mycart_add, name='mycart_add'),
               url(r'^remove/(?P<product_id>\d+)/$', views.mycart_remove, name='mycart_remove'), ]
