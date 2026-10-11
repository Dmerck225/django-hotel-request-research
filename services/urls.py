from django.urls import path
from . import views

urlpatterns = [
    path("", views.submit_request, name="submit_request"),
    path("requests/", views.request_list, name="request_list"),
    path(
        "confirmation/<int:pk>/",
        views.request_confirmation,
        name="request_confirmation",
    ),
]