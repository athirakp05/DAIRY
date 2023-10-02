from django.shortcuts import render,redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.contrib.auth import authenticate

# Create your views here.
def index(request):
    return render(request,'index.html')
#def store(request):
 #   return render(request,'store.html')
def loginn(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user) 
            return redirect('c_dash')
        else:
            messages.info(request, "Invalid login credentials")
            return redirect('login')

    return render(request,'login.html')

def register(request):
    if request.method == "POST":
        username = request.POST.get('username')
        firstname=request.POST.get('firstname') 
        lastname = request.POST.get('lastname')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirmPassword = request.POST.get('confirmPassword')

        if User.objects.filter(username=username).exists():
            messages.info(request,"username already exists!")
        elif password != confirmPassword:
            messages.info(request, "Passwords do not match")
            return redirect('registration')
      
        elif User.objects.filter(email=email).exists():
            messages.info(request,"email already used!")
            return redirect('registration')
        else:
          user = User.objects.create_user(username=username,firstname=firstname,lastname=lastname,email=email,role='CUSTOMER')
          user.set_password(password)
          user.save()
          messages.success(request,"Registered successfully")
          return redirect('login')
    return render(request,'registration.html')



def logout(request):
    auth.logout(request)
    return redirect("/")
def c_dash(request):
    return render(request,'c_dash.html')