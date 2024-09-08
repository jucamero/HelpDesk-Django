from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth import get_user_model
from django.contrib.auth import logout

User = get_user_model()

@login_required
@user_passes_test(lambda u: u.is_superuser)
def admin_user(request):
    if request.method == 'POST':
        # Verificar si se solicitó eliminar un usuario
        if 'delete_user_id' in request.POST:
            user_id = request.POST['delete_user_id']
            user = User.objects.get(pk=user_id)
            user.delete()  # Eliminar el usuario
            return redirect('admin_user')  # Redirigir a la misma página después de eliminar
        
        # Si no es eliminación, es una actualización de roles
        for user_id in request.POST.getlist('user_id'):
            user = User.objects.get(pk=user_id)
            role = request.POST.get(f'role_{user_id}')
            if role:
                user.role = role
                user.save()
        return redirect('admin_user')
    
    users = User.objects.all()
    roles = User.ROLE_CHOICES  # Pasa las opciones de rol al template
    return render(request, 'tickets/admin_user.html', {'users': users, 'roles': roles})

# Lógica de logout
def logout_view(request):
    logout(request)
    return redirect('login')
