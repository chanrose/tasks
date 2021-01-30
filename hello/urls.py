from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
   # path("broset", views.broset, name="broset"),
    path("<str:name>", views.greet, name="greet")
]

