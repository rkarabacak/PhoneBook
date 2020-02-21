from django.urls import path, include, re_path
from book.views import bookListView, bookCreateView, inline_Create_contacts, bookUpdateView

app_name = "book"

urlpatterns = [
    re_path(r'^index/$', bookListView.as_view(), name='index'),
    re_path(r'^create/$', bookCreateView.as_view(), name='create'),
    path('create2/<getNumber>/', inline_Create_contacts, name='create2'),
    path('update/<pk>/', bookUpdateView.as_view(), name='update'),
    # re_path(r'^delete/$', delete_view, name='delete'),
]
