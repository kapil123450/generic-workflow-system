from django.shortcuts import render , redirect
from django.http import HttpResponse
from .models import Post
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.messages import constants as messages
from django.contrib import messages
from django.contrib.auth import authenticate ,logout ,login
# Create your views here.

#def index(request):
#    return render(request, 'utility/index.html')

def registration(request):
    return render(request, 'utility/registration.html')   


def form(request):
    if request.method == 'POST':
            if request.POST.get('name') and request.POST.get('email') and request.POST.get('password'):
                post=Post()
                post.name= request.POST.get('name')
                print(post.name)
                post.email_address= request.POST.get('email')
                post.password= request.POST.get('password')
                if User.objects.filter(username = request.POST.get('email') ).exists():
                    messages.info(request, 'username Taken')
                    return redirect('registration')
                else:

                    user = User.objects.create_user(
                        username = request.POST.get('email'),
                        password = request.POST.get('password')
                    )
                    post.save()
                    
                    return HttpResponse('HEllo aman')

            else:
                return HttpResponse("hello aman")

def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        print('aman')
        x = True
        if x:
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(username=username, password=password)
            print(username)
            print(password)
            print(user)
            if user is not None:
                login(request, user)
                #messages.info(request, f"You are now logged in as {username}")
                return HttpResponse("hello aman you are logged in")
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    print('kumar')
    form = AuthenticationForm()
    return render( request, 'utility/index.html')
                    
    