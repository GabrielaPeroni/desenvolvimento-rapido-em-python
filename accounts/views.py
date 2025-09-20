from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import logout as django_logout
from .models import Credential
from django.http import JsonResponse


def login_view(request):
    next_page = request.GET.get('next', '/')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            cred = Credential.objects.get(username=username)
            if cred.check_password(password):
                request.session['username'] = username
                return redirect(request.POST.get('next', '/'))
            else:
                messages.error(request, "Invalid password")
                return redirect(request.path + f"?next={next_page}")
        except Credential.DoesNotExist:
            messages.error(request, "No account found")

    return render(request, 'accounts/login_page.html', {'next': next_page})


def logout_view(request):
    next_page = request.GET.get('next', '/')
    if 'username' in request.session:
        del request.session['username']
    return redirect(next_page)

def check_username_view(request):
    username = request.GET.get('username', '')
    exists = Credential.objects.filter(username=username).exists()
    return JsonResponse({'exists': exists})

def register_view(request):
    next_page = request.GET.get('next', '/')
    prefill_username = request.GET.get('username', '')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        if Credential.objects.filter(username=username).exists():
            messages.error(request, "Username already taken")
            return redirect(request.path + f"?next={next_page}")

        # Create new user
        user = Credential(username=username)
        user.set_password(password)
        user.save()

        # Log in the user
        request.session['username'] = username
        return redirect(request.POST.get('next', '/'))

    return render(request, 'accounts/register_page.html', {
        'next': next_page,
        'prefill_username': prefill_username
    })
