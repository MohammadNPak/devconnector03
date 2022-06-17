from email import message
from django.shortcuts import get_object_or_404, render,redirect
from django.http import Http404, HttpResponse
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.contrib import messages

from accounts.models import User,Experience
from .forms import UserForm,ExperienceForm

def login_page(request):
    if request.method == "POST":
        username=request.POST.get("username")
        password=request.POST.get("password")
        user = authenticate(username=username,password=password)
        # print(dir(request))
        if user:
            login(request,user)
            return redirect(to=reverse('dashboard'))
        else:
            messages.add_message(request,messages.ERROR,"username or password is wrong!")
        # print(username,password)
    return render(request,'accounts/login.html',{})

def logout_page(request):
    logout(request)
    return redirect(to=reverse('index'))

def profiles(request):
    return render(request,'accounts/profiles.html',{})

def profile(request,username):
    user=get_object_or_404(User,username=username)
    return render(request,'accounts/profile.html',{"user":user})


def register(request):
    if request.method == "POST":
        form=UserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request,messages.SUCCESS,"Your account has been created successfully! you can now login")
            return redirect(to=reverse('login'))
        else:
            return render(request,'accounts/register.html',{'form':form})

    elif request.method == "GET":
        form = UserForm()
        return render(request,'accounts/register.html',{'form':form})
    else:
        return HttpResponse("404")

@login_required
def dashboard(request):
    if request.method=="GET":
        experiences=request.user.experience_set.all()
        return render(request,'accounts/dashboard.html',{"experiences":experiences})

  
def create_profile(request):
    return render(request,'accounts/create-profile.html',{})

def add_education(request):
    return render(request,'accounts/add-education.html',{})

@login_required
def add_experience(request):
    if request.method=="POST":
        form = ExperienceForm(request.POST)
        if form.is_valid():
            form=form.save(commit=False)
            form.user=request.user
            form.save()
            messages.add_message(request,messages.SUCCESS,"your expreience has been saved successfully")
            return redirect(reverse("dashboard"))
        else:
            return render(request,'accounts/add-experience.html',{"form":form})
            
    elif request.method =="GET":
        form = ExperienceForm()
        return render(request,'accounts/add-experience.html',{"form":form})
    else:
        return HttpResponse("404")
    
@login_required
def delete_experience(request,id):

    if request.method=="POST":
        Experience.objects.get(id=id).delete()
        messages.add_message(request,messages.SUCCESS,"experience has been removed")
        return redirect(reverse("dashboard"))
    # except:
    #     return  HttpResponse("404") 
        
@login_required
def update_experience(request,id):

    e=Experience.objects.get(id=id)
    if request.method=="GET":
        # print(e)
        # print(type(e))
        f = ExperienceForm(instance=e)
        # messages.add_message(request,messages.SUCCESS,"experience has been removed")
        return render(request,'accounts/add-experience.html',{"form":f})
    elif request.method == "POST":
        form = ExperienceForm(request.POST)
        if form.is_valid():
            if e.user.id==request.user.id:
                form=form.save(commit=False)
                form.user=request.user
                form.id=id
                form.save()
            messages.add_message(request,messages.SUCCESS,"your expreience has been saved successfully")
            return redirect(reverse("dashboard"))
        else:
            return render(request,'accounts/add-experience.html',{"form":form})
        


