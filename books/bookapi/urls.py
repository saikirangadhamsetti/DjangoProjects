from django.urls import path
from . import views

urlpatterns=[
    path("bookslist/",views.BookList.as_view()),
    path("",views.BookCreate.as_view()),
    path("book/<int:id>",views.SelectedBook.as_view())
]