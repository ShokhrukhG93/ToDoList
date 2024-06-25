from django.urls import path
from .views import ListToDo, DetailToDo


urlpatterns = [
    path("", ListToDo.as_view(), name="get_tasks"),
    path("<int:pk>", DetailToDo.as_view(), name="detail_task"),
]