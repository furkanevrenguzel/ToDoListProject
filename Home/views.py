from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .forms2 import ToDoListForm
from .forms import ToDoItemForm
from .models import ToDoList,Items

from .models import Items,ToDoList
from django.contrib.auth.decorators import login_required
from .myClass import Counter
# Create your views here.



def Home(request):
    listem=ToDoList.objects.filter(author=request.user)
    flag=True
    context={}
    if not listem:
        #boşsa
        flag=False
        context={
            "flag":flag
        }
        return render(request, "index.html",context)
    else:
        #değilse  2  3

    
        datas=[]
        for i in range(0,len(listem)): # 2     0 1 2         0 1 2 3
            # fenerbahçeye ait olanları filitrele
            datas.append([Items.objects.filter(todolist=listem[i])])

            
        counter=Counter()
        counter.sifirla()
        context = {
            "listem": listem,
            "datas": datas,
            "flag":flag,
            "uzunluk":range(len(listem)),
            "counter":counter.deger,
            "degisken":counter,
            "range":range(10),
            "dizuzun":len(listem),
            "denet":True
        }
        
        return render(request,"index.html",context)


@login_required(login_url="user:login")
def deleteItem(request,id):
    data=get_object_or_404(Items,id=id)
    data.delete()
    messages.success(request, "Successfully deleted")
    return redirect("index")


@login_required(login_url="user:login")
def deleteList(request,id):
    data=get_object_or_404(ToDoList,id=id)
    data.delete()
    messages.success(request, "Successfully deleted")
    return redirect("index")


@login_required(login_url="user:login")
def updatee(request,id):
    veri=get_object_or_404(Items,id=id)
    veri.durum=True
    veri.save()
    return redirect("index")


@login_required(login_url="user:login")
def yapadd(request):
    form = ToDoListForm(request.POST or None)
    if form.is_valid():
        toDoList=form.save(commit=False)
        toDoList.author=request.user
        print(request.user)
        form.save()
        messages.success(request, "Successful")
        return redirect("One")
    return render(request, "yap-add.html", {"form": form})


@login_required(login_url="user:login")
def yapitem(request):

    listem = ToDoList.objects.filter(author=request.user)
    
    if request.method=="POST":
        form = ToDoItemForm(request.POST)
        
        if form.is_valid():
            veri=form.save(commit=False)
            veri.author=request.user
            form.save()
            messages.success(request, "Successful")
            return redirect("index")
        return render(request,"yapitem.html",{"form":form})
    else:
        if len(listem)==0:
            messages.info(request,"Add to do list")
            return redirect("yapadd")
        else:
            form = ToDoItemForm()
            form.fields["todolist"].queryset = ToDoList.objects.filter(
            author=request.user)
            return render(request, "yapitem.html", {"form": form})






