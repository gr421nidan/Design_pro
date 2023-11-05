from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth import login
from django.shortcuts import render
from django.shortcuts import redirect
from django.views.generic import CreateView
from django.views.generic import DeleteView
from .forms import RegistrationForm
from .models import CustomUser, Application
from django.contrib.auth.mixins import LoginRequiredMixin


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


class ApplicationsView(generic.ListView):
    model = Application
    template_name = 'applications.html'
    context_object_name = 'application'


class MyRequestView(LoginRequiredMixin, generic.ListView):
    model = Application
    template_name = 'my_request.html'
    context_object_name = 'application'

    def get_queryset(self):
        return Application.objects.filter(user=self.request.user)


class GetRequest(CreateView):
    model = Application
    fields = ['name', 'description', 'category', 'image']
    template_name = 'get_request.html'
    success_url = reverse_lazy('my_request')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


