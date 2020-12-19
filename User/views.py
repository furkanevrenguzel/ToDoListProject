from django.shortcuts import render, redirect

# Create your views here.
from .forms import RegisterrFormm, LoginForm

from django.contrib.auth.models import User

from django.contrib.auth import login, authenticate, logout

from django.contrib.auth.decorators import login_required

from django.contrib import messages



def Login(request):

    if request.user.is_authenticated == 1:
        return redirect("index")
    else:
        if request.method == "POST":
            formum = LoginForm(request.POST)
            if formum.is_valid():
                username = formum.cleaned_data.get("username")
                password = formum.cleaned_data.get("password")
                kullanici = authenticate(username=username, password=password)
                if kullanici is None:
                    messages.info(request, "parola veya şifre hatalı")
                    return render(request, "login.html", {"form": formum})
                login(request,kullanici)
                messages.success(request, "Giriş Yaptınız")
                return redirect("index")
            return render(request, "login.html", {"form": formum})
        else:
            form = LoginForm()
            return render(request, "login.html", {"form": form})


def registerr(request):
    if request.method == "POST":
        form = RegisterrFormm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            newUser = User(username=username)
            newUser.set_password(password)
            newUser.save()
            #login(request,newUser)
            login(request,newUser)
            messages.success(
                request, "Başarı ile Kayıt oldunuz Giriş Sayfasına Yönlendiriliyorsunuz ...")
            return redirect("One")
        return render(request, "register.html", {"form": form})
    else:
        form = RegisterrFormm()
        return render(request, "register.html", {"form": form})


@login_required(login_url="user:login")
def Logout(request):
    logout(request)
    messages.warning(request, "Çıkış Yapıldı")
    return redirect("One")
