from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from .forms import SignUpForm
from .models import VisitCount


def home_view(request):
    return render(request, 'home.html')


def signup_view(request):
    if request.user.is_authenticated:
        return redirect('visit_counter')
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('visit_counter')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})


def login_view(request):
    if request.user.is_authenticated:
        return redirect('visit_counter')
    error = None
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('visit_counter')
        else:
            error = 'Invalid username or password.'
    return render(request, 'login.html', {'error': error})


def logout_view(request):
    logout(request)
    return redirect('login')


@login_required
def visit_counter_view(request):
    visit, created = VisitCount.objects.get_or_create(user=request.user)
    visit.count += 1
    visit.save()
    return render(request, 'visit_counter.html', {'count': visit.count})
