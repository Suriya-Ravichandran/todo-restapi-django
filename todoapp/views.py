from django.shortcuts import render,HttpResponse,redirect
import requests
from django.contrib import messages
# Create your views here.
def index(request):
    if request.method == "POST":
        data = request.POST
        api_url = "http://127.0.0.1:8000/api/createtodo"
        response = requests.post(api_url, data=data)
        messages.success(request, "Todo Created success...")
        return redirect("todoapp:index")
    all_todo_api_url="http://127.0.0.1:8000/api/showtodos"
    todos = requests.get(all_todo_api_url).json()
    return render(request,'index.html',{"todos":todos})
