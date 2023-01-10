from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpRequest
from .models import Todoapp

# Create your views here.
def todo_list(request):
    all_data={'todo_list':Todoapp.objects.all()}
    return render(request, 'todoapp/todo_list.html',all_data)


def insert_todo(request:HttpRequest):
    todo=Todoapp(content=request.POST['content'])
    todo.save()
    return redirect('/list')

def delete_todo_item(request,todo_id):
    delete_id=Todoapp.objects.get(id=todo_id)
    delete_id.delete()
    return redirect('/list')