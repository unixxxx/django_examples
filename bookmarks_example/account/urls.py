from django.conf.urls import url
from django.contrib.auth import views as auth_views
from . import views


urlpatterns = [ 
    #login-logout
    url(r'^login/$', auth_views.login, name='login'),
    url(r'^logout-then-login/$', auth_views.logout_then_login, name='logout'),

    #update password
    url(r'^password-change/$', auth_views.password_change, {'template_name': 'password_change_form.html'}, name='password_change'),
    url(r'^password-change/done/$' ,auth_views.password_change_done, {'template_name': 'password_change_done.html'}, name='password_change_done'),

    #restore password
    url(r'^password-reset/$', auth_views.password_reset, {'template_name': 'password_reset_form.html'}, name='password_reset'),
    url(r'^password-reset/done/$', auth_views.password_reset_done, {'template_name': 'password_reset_done.html'}, name='password_reset_done'),
    url(r'^password-reset/confirm/(?P<uidb64>[-\w]+)/(?P<token>[-\w]+)/$', auth_views.password_reset_confirm, {'template_name': 'password_reset_confirm.html'}, name='password_reset_confirm'),
    url(r'^password-reset/complete/$', auth_views.password_reset_complete, {'template_name': 'password_reset_complete.html'}, name='password_reset_complete'),

    #registration
    url(r'^register/$', views.register, name='register'),

    #edit profile
    url(r'^edit/$', views.edit, name='edit'),

    #users
    url(r'^users/follow/$', views.user_follow, name='user_follow'),
    url(r'^users/$', views.user_list, name='user_list'),
    url(r'^users/(?P<username>[-\w]+)/$', views.user_detail, name='user_detail'),
    
    #dashboard
    url(r'^$', views.dashboard, name='dashboard'),
]
