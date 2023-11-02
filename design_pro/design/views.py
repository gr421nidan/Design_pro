from django.contrib.auth import login
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect

from .forms import  RegistrationForm
from .models import CustomUser


def base(request):
    return render(request, 'base.html')


# def register(request):
#     if request.method == 'POST':
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('login')
#     else:
#         form = UserCreationForm()
#     return render(request, 'registration/register.html', {'form': form})
#
# #
# def register(request):
#     if request.method == 'POST':
#         form = CustomUserCreationForm(request.POST)  # Используйте свою собственную форму регистрации
#         if form.is_valid():
#             form.save()
#             return redirect('login')
#     else:
#         form = CustomUserCreationForm()  # Используйте свою собственную форму регистрации
#     return render(request, 'registration/register.html', {'form': form})
def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            full_name = form.cleaned_data['full_name']
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = CustomUser.objects.create_user(username, email, password)
            user.first_name = full_name
            user.save()
            login(request, user)
            return redirect('base')
    else:
        form = RegistrationForm()

    return render(request, 'registration/register.html', {'form': form})

