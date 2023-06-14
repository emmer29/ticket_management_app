from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout 
from .forms import RegisterCustomerForm

# Create your views here.

def register_customer(request):
    if request.method == 'POST':
        form = RegisterCustomerForm(request.POST)
        if form.is_valid():
            var = form.save(commit=False)
            var.is_customer = True
            var.save()
            messages.info(request, 'Your account has been successfully registered. Please login to continue')
            return redirect('login')
        else:
            # Print the custom password error message
            password_errors = form.errors.get('password2')
            if password_errors:
                for error in password_errors:
                    print('Make sure your passwords dont look like username and should have at least 8 characters:', error)
            messages.warning(request, "Something went wrong, please check the form input")
    else:
        form = RegisterCustomerForm()

    context = {'form': form}
    return render(request, 'users/register_customer.html', context)

#login a user
def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None and user.is_active:
            login(request, user)
            messages.info(request, 'login successful. please enjoy your session')
            return redirect('dashboard')
        else:
            messages.warning(request, 'something went wrong, check form input')
            return redirect('login')
    else:
        return render(request, 'users/login.html')
        
#logout a user
def logout_user(request):
    logout(request)
    messages.info(request, 'your session has ended, please login to continue')
    return redirect('login')


         