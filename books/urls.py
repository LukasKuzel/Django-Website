from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('booklist/', views.BookListView.as_view(), name='booklist'),
    path('authorlist/', views.AuthorListView.as_view(), name='authorlist'),
    path('booklist/<int:pk>/', views.BookDetailView.as_view(), name='bookdetail'),
    path('authorlist/<int:pk>/', views.AuthorDetailView.as_view(), name='authordetail'),
    path('booklist/genres/<str:genre_name>/', views.BookListView.as_view(), name='bookgenre'),
    path('booklist/kinds/<str:kind_name>/', views.BookListView.as_view(), name='bookkind'),
    path('booklist/authors/<str:author_name>/', views.BookListView.as_view(), name='bookauthor'),
]