from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib import messages

def about(request):
    return render(request, 'about.html')



def teacher_login_view(request):
    if request.method == 'POST':
        u = request.POST.get('username')
        p = request.POST.get('password')
        
        user = authenticate(request, username=u, password=p)
        
        if user is not None:
            login(request, user)
            # Redirect to the 'dashboard' name in teacher/urls.py
            return redirect('teacher_dashboard') 
        else:
            messages.error(request, "Invalid username or password.")
            
    return render(request, 'teacher/teacher_login.html')
# Create your views here.

