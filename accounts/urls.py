from django.urls import re_path
from accounts.views import signup_view, login_view, logout_view


app_name = "accounts"

urlpatterns = [
    re_path(r'^login/$', login_view, name='login'),
    re_path(r'^logout/$', logout_view, name='logout'),
    re_path(r'^signup/$', signup_view, name='signup'),
]