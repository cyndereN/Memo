from django.urls import path

from . import views

app_name = "To_do"

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:topic_id>", views.topic, name = "topic"),
]