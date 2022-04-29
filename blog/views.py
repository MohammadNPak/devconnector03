from django.shortcuts import render

# Create your views here.


# def my_view(request):
#     return render(request,'',{})

def index(request):
    context = {}
    return render(request,'blog\index.html',context)