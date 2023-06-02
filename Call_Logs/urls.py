from django.urls import path, include, re_path
from Call_Logs.views import callLogsView, callLogsCreateView, calllogsDetailView #, search_view

app_name = "calllogs"

urlpatterns = [
    re_path(r'^index/$', callLogsView.as_view(), name='index'),
    re_path(r'^create/$', callLogsCreateView.as_view(), name='create'),
    path('<int:pk>/', calllogsDetailView.as_view(), name='detail'),
    # re_path(r'^(?P<data>\w+)$', search_view, name='search2'),
    # path('search/<data>/', search_view, name='search'),
    # re_path(r'^update/$', update_view, name='update'),
    # re_path(r'^delete/$', delete_view, name='delete'),
]