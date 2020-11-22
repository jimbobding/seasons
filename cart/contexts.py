from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from products.models import Product
from subscriptions.models import Size


def cart_contents(request):

    cart_items = []
    total = 0 
    size_count = 0
    product_count = 0
    cart = request.session.get('cart', {})

    for product_id, item_data in cart.items():
        if isinstance(item_data, int):
            product = get_object_or_404(Product, pk=product_id)
            total += item_data * product.price
            product_count += item_data
            cart_items.append({
                'product_id': product_id,
                'quantity': item_data,
                'product': product,
            })
        else:
            size = Size.objects.all()
            for quantity in item_data['size'].items():
                item_id = size.id
                total += quantity * size.price
                size_count += quantity
                cart_items.append({
                    'item_id': item_id,
                    'quantity': quantity,
                    'product': product,
                    'size': size,
                })

    if total < settings.FREE_DELIVERY_THRESHOLD:
        delivery = total * Decimal(settings.STANDARD_DELIVERY_PERCENTAGE / 100)
        free_delivery_delta = settings.FREE_DELIVERY_THRESHOLD - total
    else:
        delivery = 0
        free_delivery_delta = 0

    grand_total = delivery + total

    context = {
        'cart_items': cart_items,
        'total': total,
        'product_count': product_count,
        'size_count': size_count,
        'delivery': delivery,
        'free_delivery_delta': free_delivery_delta,
        'free_delivery_threshold': settings.FREE_DELIVERY_THRESHOLD,
        'grand_total': grand_total
    }

    return context


"""def cart_size_contents(request):

    cart_items = []
    total = 0
    size_count = 0

    cart = request.session.get('cart', {})

    for size_id, item_data in cart.items():
        if isinstance(item_data, int):
            size = get_object_or_404(Size, pk=size_id)
            total += item_data * size.price
            size_count += item_data
            cart_items.append({
                'size_id': size_id,
                'quantity': item_data,
                'size': size,
            })
        else:
            size = get_object_or_404(Size, pk=size_id)
            for size, quantity in item_data['items_by_size'].items():
                total += quantity * size.price
                size_count += quantity
                cart_items.append({
                    'size_id': size_id,
                    'quantity': quantity,
                    'size': size,
                })

    if total < settings.FREE_DELIVERY_THRESHOLD:
        delivery = total * Decimal(settings.STANDARD_DELIVERY_PERCENTAGE / 100)
        free_delivery_delta = settings.FREE_DELIVERY_THRESHOLD - total
    else:
        delivery = 0
        free_delivery_delta = 0

    grand_total = delivery + total

    context = {
        'cart_items': cart_items,
        'total': total,
        'size_count': size_count,
        'delivery': delivery,
        'free_delivery_delta': free_delivery_delta,
        'free_delivery_threshold': settings.FREE_DELIVERY_THRESHOLD,
        'grand_total': grand_total
    }

    return context"""
