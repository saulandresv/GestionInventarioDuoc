from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages

def login_view(request):
    if request.method == 'POST':
        # Get username and password from POST data
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Attempt to authenticate the user
        user = authenticate(request, username=username, password=password)
        if user is not None:
            # If authentication is successful, log the user in
            login(request, user)
            messages.success(request, "Has iniciado sesión con éxito.")
            return redirect('gestionInventario')  # Replace 'homepage' with your desired route
        else:
            # If authentication fails, show an error message
            messages.error(request, "Nombre de usuario o contraseña incorrectos.")

    # If the request is GET or authentication fails, re-render the login page
    return render(request, 'login/login.html')
