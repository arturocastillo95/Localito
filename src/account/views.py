from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from account.forms import RegistrationForm

def registerView(request):
    context = {}

    if request.POST:
        form = RegistrationForm(request.POST)
        if form.is_valid:
            new_user = form.save()
            email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')
            account = authenticate(email=email, password=raw_password)
            login(request, account)
            return redirect('dashboard')
        else:
            context['registration_form'] = form
    else:
        form = RegistrationForm()
        context['registration_form'] = form
    
    return render(request, 'account/register.html', context)

