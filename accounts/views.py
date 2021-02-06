from django.shortcuts import render, redirect
from django.views.generic import TemplateView, FormView
from django.contrib.auth import authenticate, login, logout

from .forms import RegisterForm

# Create your views here.


def login_view(request):
    if request.method == "POST":
        email = request.POST["email"]
        password = request.POST["password"]
        user = authenticate(email=email, password=password)
        if user:
            login(request, user)
            return redirect('posts:home')
        else:
            return render(request, "accounts/login.html", {'error': True})
    
    return render(request, "accounts/login.html")


class RegisterView(FormView):
    template_name = "accounts/register.html"
    form_class = RegisterForm

    def form_valid(self, form):
        form.save()
        return redirect("/")

def logout_view(request):
    logout(request)
    return redirect('accounts:login')