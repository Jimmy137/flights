from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.flights, name="fls"),
    path("<int:id>", views.flight, name="fl"),
    path("<int:id>/book", views.book, name="book")
]