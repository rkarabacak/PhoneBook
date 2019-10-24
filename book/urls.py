from django.urls import path, include, re_path
from book.views import bookListView, bookCreateView

app_name = "book"

urlpatterns = [
    re_path(r'^index/$', bookListView.as_view(), name='index'),
    re_path(r'^create/$', bookCreateView.as_view(), name='create'),
    # re_path(r'^update/$', update_view, name='update'),
    # re_path(r'^delete/$', delete_view, name='delete'),
]
