from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import  messages
from .forms import UserRegisterForm, BuyerShippingForm, UserUpdateForm


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Konto o nazwie {username} zostało pomyślnie utworzone! Zaloguj się!')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form':form})


@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        if u_form.is_valid():
            u_form.save()
            messages.success(request, f'Informacje zostały zaktualizowane')
            return redirect('profile')

    else:
        u_form = UserUpdateForm(instance=request.user)

    context = {
        'u_form':u_form
    }

    return render(request, 'users/profile.html',context)

@login_required
def transaction_history(request):
    return render(request, 'users/profile.html')



def shipping_form(request):
    s_form = BuyerShippingForm()

    context = {
        's_form':s_form
    }

    return render(request, 'users/shipping.html', context)