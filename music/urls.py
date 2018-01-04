from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.createpost, name='index'),
    url(r'books/$', views.createbooks, name='book'),
    url(r'books/(?P<bookname>[a-zA-z]+)$', views.bookview, name='bookview'),
    url(r'(?P<authorname>[a-zA-z]+)$', views.booklist, name='booklist'),
]
