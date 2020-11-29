from django.shortcuts import render, get_object_or_404
from .models import Subscriptions, Size
from products.models import Product


def subscriptions(request):
    """ A view to the subscriptions page  """

    subscriptions = Subscriptions.objects.all()
    context = {
        'subscriptions': subscriptions,
 
    }
    print(size)
    return render(request, "subscriptions/subscriptions.html", context)


def subscription_detail(request, subscriptions_id):
    """ A view to the selected  subscription """
    product = Product.objects.filter(is_a_subscription='True')
    product_s = product.filter(season='spring')
    subscription = get_object_or_404(Subscriptions, pk=subscriptions_id)
    #subscription_s = subscription.objects.all()
    #sub_season = subscriptions.filter(season='season')

    context = {
        'subscription': subscription,
        'product': product,
        #'sub_season': sub_season,
    }
    
    #print(subscription_s)
    print(product)
    print(subscription)
    return render(request, "subscriptions/subscription_detail.html", context)


def size(request, subscriptions_id):
    """ A view to the selected  subscription """

    size = Size.objects.all()
    context = {
        'size': size,
    }

    return render(request, "subscriptions/subscription_detail.html", context)


#def season_product_match(request, season_id):

 #   prod_subscription = Product.objects.filter(is_a_subscription=True)
#    season = prod_subscription.filter('season')
# sub_season = Subscriptions.objects.filter('season')

#     context = {
#      ' season': season,
#       'sub_season': sub_season,
#      }


#    return render(request, "subscriptions/subscription_detail.html", context) 