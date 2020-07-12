from django.contrib.auth import authenticate, login
from django.shortcuts import redirect, render

from .forms import UserLoginForm


def login_view(request):
    next = request.GET.get('next')
    form = UserLoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        login(request, user)
        if next:
            return redirect(next)
        return redirect('')

    context = {
        'form': form
    }

    return render(request, 'login.html', context)
