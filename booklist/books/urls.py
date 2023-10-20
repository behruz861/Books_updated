from django.urls import path
from . import views

urlpatterns = [
    path('', views.book_list, name='book_list'),
    path('create/', views.book_create, name='book_create'),
    path('<slug:slug>/', views.book_detail, name='book_detail'),
    path('<slug:slug>/update/', views.book_update, name='book_update'),
    path('<slug:slug>/delete/', views.book_delete, name='book_delete')
]