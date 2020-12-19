

from django.urls import path
from . import views

app_name = "user"

urlpatterns = [
    path('register/', views.registerr, name="register"),
    path('login/', views.Login, name="login"),
    path('logout/', views.Logout, name="logout")
]
