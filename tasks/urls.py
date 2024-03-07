from django.urls import path

from . import views

urlpatterns = [
    path("", views.StartingPage.as_view(), name="tasks"),
    path('task/<int:pk>/', views.TaskDetail.as_view(), name='task_detail'),
    path('create_task/', views.CreateTask.as_view(), name="task_create")
]
