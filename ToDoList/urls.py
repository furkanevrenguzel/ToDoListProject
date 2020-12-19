"""list URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from Home.views import yapadd, yapitem, Home,deleteItem,deleteList,updatee
from user.views import Login
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Login, name="One"),
    path('my/yapadd/', yapadd, name="yapadd"),
    path('my/yapitem', yapitem, name="yapitem"),
    path('Home/', Home, name="index"),
    path('user/', include("user.urls")),
    path('delete/<int:id>',deleteItem,name="deleteItem"),
    path('deleteList/<int:id>',deleteList,name="deleteList"),
    path('update/<int:id>',updatee,name="update"),
    
]
