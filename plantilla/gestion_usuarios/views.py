from django.contrib import messages
from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.models import User, auth
from .models import User

def salir(request):
    auth.logout(request)
    return redirect('home')

def inicio_sesion(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            if user.grupo == "Administradores":
                return redirect('/admin')
            else:
               return redirect('vista_usuarios')
        else:
            messages.info(request, 'Usuario y/o Clave Invalida')
            return redirect('inicio_sesion')

    else:
        return render(request, 'login.html')

def registrar_usuario(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        grupo = request.POST['grupo']

        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Usuario ya registrado.')
                return redirect('registrar_usuario')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email ya está registrado.')
                return redirect('registrar_usuario')
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.grupo = grupo
                user.save()
                return redirect('inicio_sesion')

        else:
            messages.info(request, 'Las contraseñas no coinciden.')
            return redirect('registrar_usuario')

    else:
        return render(request, 'registro.html')

def home(request):
    return render(request, 'home.html')

def vista_usuarios(request):
    return render(request, 'usuario.html')