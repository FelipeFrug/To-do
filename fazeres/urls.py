# fazeres/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ToDoViewSet, todo_list, todo_detail, todo_create, todo_update, todo_delete

router = DefaultRouter()
router.register(r'todos', ToDoViewSet)

urlpatterns = [
    path('', todo_list, name='todo_list'),
    path('api/', include(router.urls)),
    path('todo/<int:pk>/', todo_detail, name='todo_detail'),
    path('todo/new/', todo_create, name='todo_create'),
    path('todo/<int:pk>/edit/', todo_update, name='todo_update'),
    path('todo/<int:pk>/delete/', todo_delete, name='todo_delete'),
]