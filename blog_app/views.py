from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import auth, User
from django.contrib import messages
from django.contrib.auth import authenticate
from .models import Blog

import random
 

def register (request):
        
    if request.method == 'POST':
            
        username=request.POST.get('r_name', '').lower()
        email=request.POST.get('r_email', '').lower()
        password=request.POST.get('r_password', '')
        password2=request.POST.get('r_password2', '.')
        generate_password=request.POST.get('generate','.')


        if password == password2:
            if User.objects. filter(email=email).exists():
                messages.info(request, 'This Email is already in use!')
                
            elif User.objects.filter(username=username).exists():
                messages.info(request, 'This Username is already in use!')
                
            else:
                user=User.objects.create_user(username=username, email=email, password=password)
                user.save(); 
                return redirect ('login')
            
        else:
            messages.info(request, 'These passwords do not match!')

        if generate_password:            
            r_password=''

            characters=['qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM0123456789$%^&*(_-+=']    

            for _ in range(10):
                r_password+=str(random.choice(characters))

        r_context={
            'random_password':r_password
            }
        
        #Prepare code for email authentication 
    
        return render(request, 'register.html', {'register_context':r_context})
    

    


def login(request):
    if request.method=='POST':
        username=request.POST.get('l_username', '')
        password=request.POST.get('l_password', '')

        log_in_context={
            "username":username,
            "password": password, 
        }

        user=auth.authenticate(username=username, password=password)

        if user:
            is_authenticate=True
            if user is not None:
                auth.login(request, user)

                #Prepare email for sending notification to user
                
                return render ('index.html', {"l_context":log_in_context, 'is_authenticate': True})
    
    return render(request, 'login.html')



def index (request):
    posts=Blog.objects.all()
    return render (request, 'index.html', {'i_post':posts})



def dynamic_posts(request, pk):
    posts=Blog.objects.get(id=pk)
    return render(request, 'posts.html', {'p_posts':posts})

def posts(request):
    return render(request, 'posts.html')




