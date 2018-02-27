from django.shortcuts import render, redirect
from django.contrib.auth.forms import PasswordChangeForm
from .form import JoinFormUser, JoinFormProfile
from django.contrib.auth import authenticate, login
from .models import T_Profile
from django.contrib.auth.models import User

def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            return HttpResponseRedirect('/')
        else:
            return HttpResponseRedirect('/password/')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'accounts/change_password.html', {
        'form': form
    })

def join(request):
    if request.method == 'POST':
        formsetUser = JoinFormUser(request.POST)
        formsetProfile = JoinFormProfile(request.POST)
        if formsetUser.is_valid() and formsetProfile.is_valid():
            formsetUser.save() # Save user data from form
            username = formsetUser.cleaned_data['username']
            password = formsetUser.cleaned_data['password']

            # Set up new user password
            user = User.objects.get(username=username)
            user.set_password(password)

            # Input user profile data
            hahaha = formsetProfile.cleaned_data['hahaha']

            user.t_profile.hahaha=hahaha
            user.save()

            new_user = authenticate(request, username=username, password=password)
            print(new_user)
            if user is not None:
                login(request, new_user)

            return redirect('/main/')

    else:
        formsetUser = JoinFormUser()
        formsetProfile = JoinFormProfile()
        return render(request, 'registration/join.html', {'formsetUser': formsetUser, 'formsetProfile': formsetProfile})

    return redirect('/user/login/')
