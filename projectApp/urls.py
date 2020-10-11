from django.urls import path

from projectApp import views

urlpatterns = [
    path('bookdetail/', views.project_detail, name='bookdetail'),
    path('hello', views.hello, name='Hello '),
    path('books', views.get_all_books, name="Get All Books")
]
