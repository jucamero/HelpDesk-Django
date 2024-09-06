from django.contrib.auth import login
from django.shortcuts import render, redirect
from ..forms import CustomUserCreationForm

# Vista del registro
def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home_user')  # O redirige donde prefieras
    else:
        form = CustomUserCreationForm()
    return render(request, 'tickets/register.html', {'form': form})