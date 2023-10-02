from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'index.html')
def store(request):
    return render(request,'store.html')
def loginn(request):
    return render(request,'login.html')
def register(request):
    return render(request,'registration.html')



