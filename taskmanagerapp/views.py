from django.shortcuts import render, redirect , HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate , logout
from django.contrib.auth.decorators import login_required

from taskmanagerapp.forms import TODOForm
from taskmanagerapp.models import TODO

from datetime import datetime
from taskmanagerapp.models import Contact
from django.contrib import messages

def signup(request):
    if request.method == 'POST':
        username = request.POST.get("username")
        email = request.POST.get("email")
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")
        if password1 != password2:
            return HttpResponse("Password and confirm password are mismatched")
        else:
            my_user = User.objects.create_user(username , email , password1)
            my_user.save()
            return redirect('login')

    return render(request , "signup.html"  )



# Create your views here.
def index(request):
    return render(request , "index.html"  )

def about(request):
    return render(request , "about.html")

def contact(request):
    if request.method == "POST" :
        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        desc = request.POST.get("desc")
        contact = Contact(name =name , email = email , phone = phone , desc = desc , date = datetime.today())
        contact.save()
        messages.success(request, "Your Message has been Sent 📩 ")


    return render(request , "contact.html")


def LoginPage(request):
    if request.method=='POST':
        username=request.POST.get('username')
        pass1=request.POST.get('password')
        user=authenticate(request,username=username,password=pass1)
        if user is not None:
            login(request,user)
            return redirect('dashboard')
        else:
            return HttpResponse ("Username or Password is incorrect!!!")

    return render (request,'login.html')
    


def LogoutPage(request):
    logout(request)
    return redirect("home")


@login_required(login_url="login")
def dashboard(request):
    if request.user.is_authenticated:
        user = request.user
        form = TODOForm()
        todos = TODO.objects.filter(user = user).order_by('priority')
        return render(request , 'dashboard.html' , context={'form' : form , 'todos' : todos})



@login_required(login_url='login')
def add_todo(request):
    if request.user.is_authenticated:
        user = request.user
        print(user)
        form = TODOForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            todo = form.save(commit=False)
            todo.user = user
            todo.save()
            print(todo)
            return redirect("dashboard")
        else: 
            return render(request , 'index.html' , context={'form' : form})


def delete_todo(request , id ):
    print(id)
    TODO.objects.get(pk = id).delete()
    return redirect('dashboard')

def change_todo(request , id  , status):
    todo = TODO.objects.get(pk = id)
    todo.status = status
    todo.save()
    return redirect('dashboard')


