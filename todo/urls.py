from django.urls import path
from . import views


urlpatterns = [
    path('createtodo',views.createtodo,name="createtodo"),
    path('showtodos',views.showtodos,name="showtodos")
]