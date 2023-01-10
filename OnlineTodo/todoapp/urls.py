from django.contrib import admin
from .import views
from django.urls import path,include

urlpatterns = [
    path('list/', views.todo_list),
    path('insert_todo/',views.insert_todo,name='insert_todo'),
    path('delete/<int:todo_id>',views.delete_todo_item,name='delete_todo_item')
    
]
