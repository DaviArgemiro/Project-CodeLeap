from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm

def login_view(request):
    
    if request.method == "POST":
        username = request.POST['username']
        
        user = authenticate(request, username=username, password="alienigena123")

        if user is not None:
            login(request, user=user)
            return redirect('post_list')
        else:
            login_form = AuthenticationForm()
    else:
        login_form = AuthenticationForm()

    return render(request, 'login.html', {'login_form': login_form})