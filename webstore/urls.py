from django.conf.urls import url
from . import views
from django.contrib.auth.views import (login, logout, password_reset, password_reset_done, password_reset_confirm,
                                       password_reset_complete, )

urlpatterns = [
        url(r'^$', views.home, name='home'),
        url(r'^login/$', login, {'template_name': 'webstore/login.html'}, name='login'),
        url(r'^logout/$', logout, {'template_name': 'webstore/logout.html'}, name='logout'),
        url(r'^register/$', views.register, name='register'),
        url(r'^edit_profile/$', views.edit_profile, name='edit_profile'),
        url(r'^change_password/$', views.change_password, name='change_password'),
        url(r'^reset_password/$', password_reset, {'template_name': 'webstore/reset_password.html'},
            name='reset_password'),
        url(r'^reset_password/done/$', password_reset_done, name='password_reset_done'),
        url(r'^reset_password/confirm/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$', password_reset_confirm,
            name='password_reset_confirm'),
        url(r'^reset_password/complete/$', password_reset_complete,
            name='password_reset_complete'),
]