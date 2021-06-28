from django.shortcuts import render, redirect
from .models import CustomUser
from django.views.generic import View
from .forms import UserForm, UpdateUserForm

def all_users(request):
    list_of_users = CustomUser.get_all()

    return render(request, "authentication\\all_users.html", {"list_of_users": list_of_users})

def delete(request, id):
    CustomUser.delete_by_id(id)
    return redirect('authentication:all_users')

class CreateUser(View):
    
    def get(self, request):
        form = UserForm()
        return render(request, 'authentication\\create_user_form.html', {'form': form})
    
    def post(self, request):
        bound_form = UserForm(request.POST)
        if bound_form.is_valid():
            new_user = bound_form.save()
            return redirect('authentication:all_users')
        return render(request, 'authentication\\create_user_form.html', {'form': bound_form})

class UpdateUser(View):
    def get(self, request, id):
        user = CustomUser.get_by_id(id)
        form = UpdateUserForm(instance=user)
        return render(request, 'authentication\\update_user_form.html', {'form': form, "user": user})
    def post(self, request, id):
        user = CustomUser.get_by_id(id)
        bound_form = UpdateUserForm(request.POST, instance=user)
        if bound_form.is_valid():   
            bound_form.save()
            return redirect('authentication:all_users')
        print('-'*90)
        return render(request, 'authentication\\update_user_form.html', {'form': bound_form})