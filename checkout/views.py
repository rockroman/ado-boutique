from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from .forms import OrderForm

# Create your views here.


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in your Bag at the moment")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51Mu1otHnuSLdtSyi5NC1phkRtR0eb4nxnXlX8bQpYVv3YPoBk7FAN9mDNlDz3e75pTDyWg7BTJ2s9eYikIYk5ToC0081myun6k',
        'client_secret': 'test_client_secret',
    }

    return render(request, template, context)
