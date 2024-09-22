from django.contrib.auth import login
from django.contrib import messages
from django.shortcuts import render, redirect
from ..forms import CustomUserCreationForm

# Vista del registro
def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            password1 = form.cleaned_data.get('password1')
            password2 = form.cleaned_data.get('password2')
            if password1 != password2:
                messages.error(request, "Las contraseñas no coinciden.")
            else:
                user = form.save()
                login(request, user)
                return redirect('home_user')  # O redirige donde prefieras
        else:
            messages.error(request, "Error en el formulario.")
    else:
        form = CustomUserCreationForm()
    return render(request, 'tickets/register.html', {'form': form})
