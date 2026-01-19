from django.shortcuts import render
from .models import Product

# Create your views here.

def home(request):
    products = Product.objects.all()
    total = Product.objects.count()
    denied = Product.objects.filter(state="denied")
    aproved = Product.objects.filter(state="aproved")
    pending = Product.objects.filter(state="pending")
    count_denied = denied.count()
    count_aproved = aproved.count()
    count_pending = pending.count()
    return render(request, "index.html", {'products': products, 'count_denied': count_denied, 'count_pending': count_pending, 'count_aproved': count_aproved, 'total': total})