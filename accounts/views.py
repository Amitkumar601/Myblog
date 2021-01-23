
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages



# Create your views here.
def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            messages.success(request,'You are now logged in')
            return redirect('home')
        else:
            messages.error(request,'Invalid Credantials')
            return redirect('login')
    else:
        return render(request,'accounts/login.html')
    return render(request,'accounts/login.html') 

def register(request):
    if request.method == "POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        

        if password1==password2:
           
            if User.objects.filter(username=username).exists():
                messages.error(request,'Username already taken!')

            else:
                user = User.objects.create_user( password=password1, username=username, first_name=first_name, last_name=last_name)
                user.save()
                messages.success(request, 'User is successfully registered!')
                return redirect('login')
        else:
            messages.error(request,'Password did not match!')
        return redirect('register')
    else:
        return render(request,'accounts/register.html')


def logout(request):
    auth.logout(request)
    messages.success(request,'You have been logout!!')
    return redirect("home")
   