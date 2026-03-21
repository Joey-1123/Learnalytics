from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django_ratelimit.decorators import ratelimit


def about(request):
    return render(request, 'about.html')


@ratelimit(key='post:username', rate='5/m', block=False)
def teacher_login_view(request):
    if request.method == 'POST':
        u = request.POST.get('username')
        p = request.POST.get('password')
        
        user = authenticate(request, username=u, password=p)
        
        if user is not None:
            login(request, user)
            return redirect('teacher_dashboard') 
        else:
            messages.error(request, "Invalid username or password.")
            
    return render(request, 'teacher/teacher_login.html')