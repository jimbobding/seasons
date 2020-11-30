from django.shortcuts import render
from .models import Subscriptions
from products.models import Product


def subscriptions(request):
    """ A view to the subscriptions page  """

    subscriptions = Subscriptions.objects.all()

    context = {
        'subscriptions': subscriptions,
    }

    return render(request, "subscriptions/subscriptions.html", context)


def subscription_detail(request, season):
    """ A view to the selected  subscription """

    product = Product.objects.filter(season=season)
    subscription = Subscriptions.objects.filter(season=season)

    context = {

       'product': product,
       'subscription': subscription,
    }

    return render(request, "subscriptions/subscription_detail.html", context)
