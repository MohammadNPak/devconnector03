from email import message
from django.shortcuts import get_object_or_404, render,redirect
from django.http import Http404, HttpResponse
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.utils.http import urlencode
from django.contrib import messages

from accounts.models import Education, User,Experience
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
    experiences=request.user.experience_set.all()
    return render(request,'accounts/dashboard.html',{"experiences":experiences})

  
def create_profile(request):
    return render(request,'accounts/create-profile.html',{})

@login_required
def add_education(request):
    if request.method=="POST":
        form=ExperienceForm(request.POST)
        if form.is_valid():
            form.save(commit=False)
            messages.add_message(request,messages.SUCCESS,"Your education has been added successfully!")
            return redirect(to=reverse('dashboard'))
        else:
            return render(request,'accounts/add-education.html',{'form':form})
    form = ExperienceForm()
    return render(request,'accounts/add-education.html',{'form':form})

@login_required
def update_education(request,id):
    education=get_object_or_404(Education,id=id)
    if education.user!=request.user:
        messages.add_message(request,messages.ERROR,f"You are not authorized to update {education} education!")
        return redirect(to=reverse('message'))
    if request.method=="POST":
        form=ExperienceForm(request.POST,instance=education)
        if form.is_valid():
            form.save()
            messages.add_message(request,messages.SUCCESS,"Your education has been updated successfully!")
            return redirect(to=reverse('dashboard'))
        else:
            return render(request,'accounts/add-education.html',{'form':form})
    form = ExperienceForm(instance=education)
    return render(request,'accounts/add-education.html',{'form':form})

@login_required
def delete_education(request,id):
    education=get_object_or_404(Experience,id=id)
    if education.user == request.user:
        education.delete()
        messages.add_message(request,messages.SUCCESS,"Your education has been deleted successfully!")
        return redirect(to=reverse('dashboard'))
    else:
        messages.add_message(request,messages.ERROR,f"You are not authorized to delete {education} education!")
        return redirect(to=reverse('message'))


def message(request):
    back_link=request.META.get('HTTP_REFERER',None)
    print(request.META)
    if not back_link:
        back_link = reverse('dashboard')
    return render(request,'message.html',{'back_link':back_link})


def detail_experience(request,id):
    experience=get_object_or_404(Experience,id=id)
    return render(request,'accounts/detail-experience.html',{'experience':experience})

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
    experience=get_object_or_404(Experience,id=id)
    if experience.user == request.user:
        experience.delete()
        messages.add_message(request,messages.SUCCESS,"Your experience has been deleted successfully!")
        return redirect(to=reverse('dashboard'))
    else:
        messages.add_message(request,messages.ERROR,f"You are not authorized to delete {experience} experience!")
        return redirect(to=reverse('message'))
        

@login_required
def update_experience(request,id):
    experience=Experience.objects.get(id=id)
    if experience.user.id==request.user.id:
        messages.add_message(request,messages.ERROR,f"You are not authorized to update {experience} experience!")
        return redirect(reverse('message'))
    if request.method=="GET":
        form = ExperienceForm(instance=experience)
        return render(request,'accounts/add-experience.html',{"form":form})
    elif request.method == "POST":
        form = ExperienceForm(request.POST)
        if form.is_valid():
            form=form.save(commit=False)
            form.user=request.user
            form.id=id
            form.save()
            messages.add_message(request,messages.SUCCESS,"your expreience has been saved successfully")
            return redirect(reverse("dashboard"))
        else:
            return render(request,'accounts/add-experience.html',{"form":form})
        


