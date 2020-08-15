 

"""metodos de usuarios"""


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
    return redirect('users:login')


def add_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        password2 = request.POST['password2']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']

        if password != password2:
            return render(request, 'users/registro.html', {'error': 'Las contraseñas no coinciden'})

        user = User.objects.create_user(username=username, password=password)
        user.first_name = first_name
        user.last_name = last_name
        user.email = email
        user.save()

        profile = Profile(user=user)
        profile.save()
        return redirect('users:login')

    return render(request, 'users/registro.html')


def add_superuser(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        password2 = request.POST['password2']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']

        if password != password2:
            return render(request, 'users/registro_admin.html', {'error': 'Las contraseñas no coinciden'})

        user = User.objects.create_superuser(
            username=username, password=password)
        user.first_name = first_name
        user.last_name = last_name
        user.email = email
        user.save()

        profile = Profile(user=user)
        profile.save()
        return redirect('users:login')

    return render(request, 'users/registro_admin.html')


def update_profile(request):
    profile = request.user.profile

    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            data = form.cleaned_data
            profile.phone_number = data['phone_number']
            profile.biography = data['biography']
            profile.picture = data['picture']
            profile.save()

            return redirect('users:profile')

    else:
        form = ProfileForm()

    return render(
        request=request,
        template_name='users/profile.html',
        context={
            'profile': profile,
            'user': request.user,
            'form': form
        }
    )
