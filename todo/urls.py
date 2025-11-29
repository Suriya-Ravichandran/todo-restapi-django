from django.urls import path
from . import views


urlpatterns = [
    path('createtodo',views.createtodo,name="createtodo"),
    path('showtodos',views.showtodos,name="showtodos"),
    path('getonetodo/<int:pk>',views.getonetodo,name="getonetodo"),
    path('updatetodo/<int:pk>',views.updatetodo,name="updatetodo"),
    path('deletetodo/<int:pk>',views.deletetodo,name="deletetodo"),
]
