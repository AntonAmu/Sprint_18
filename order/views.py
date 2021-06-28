from django.shortcuts import render, redirect
from .models import Order
from django.views.generic import View
from .forms import OrderForm, UpdateOrderForm

def all_orders(request):
    list_of_orders = Order.get_all()

    return render(request, "order\\all_orders.html", {"list_of_orders": list_of_orders})

def delete(request, id):
    Order.delete_by_id(id)
    return redirect('order:all_orders')

class CreateOrder(View):
    
    def get(self, request):
        form = OrderForm()
        return render(request, 'order\\create_order_form.html', {'form': form})
    
    def post(self, request):
        bound_form = OrderForm(request.POST)
        if bound_form.is_valid():
            new_order = bound_form.save()
            return redirect('order:all_orders')
        return render(request, 'order\\create_order_form.html', {'form': bound_form})

class UpdateOrder(View):
    def get(self, request, id):
        order = Order.get_by_id(id)
        form = UpdateOrderForm(instance=order)
        return render(request, 'order\\update_order_form.html', {'form': form, "order": order})
    def post(self, request, id):
        order = Order.get_by_id(id)
        bound_form = UpdateOrderForm(request.POST, instance=order)
        if bound_form.is_valid():   
            bound_form.save()
            return redirect('order:all_orders')
        print('-'*90)
        return render(request, 'order\\update_order_form.html', {'form': bound_form})