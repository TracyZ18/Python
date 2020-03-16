from django.shortcuts import render, redirect

# from django documentation
from django.contrib.auth import logout

def logout_view(request):
    logout(request)
    return redirect('/') # redirecting to root


from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm
def register(request):
    """Register a new user."""
    if request.method != 'POST':
        # Display blank registration form.
        form = UserCreationForm()
    else:
        # Process completed form.
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            new_user = form.save()
            # Log the user in and then redirect to home page.
            authenticated_user = authenticate(username=new_user.username,
            password=request.POST['password1'])
            login(request, authenticated_user)
            return redirect('/')
    context = {'form': form, 'title': "Register"}
    return render(request, 'users/register.html', context)