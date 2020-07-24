from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import redirect, render


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('recipes:index')
        else:
            return render(request, 'users/login.html', {'errors': 'El usuario y/o la contraseña no son correctos'})

    return render(request, 'users/login.html')

@login_required
def logout_view(request):
    logout(request)
    return redirect ('users:login')
