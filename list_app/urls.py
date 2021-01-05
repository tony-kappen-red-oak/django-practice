from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('loginOrSignUp',views.loginOrSignUp,name="loginOrSignUp"),
    path('<int:pk>/list_view',views.list_view,name="list_view"),
    path('<int:pk>/add-task',views.add_task,name="add-task"),
    path('save-tasks',views.save_tasks,name="save-tasks")
]
