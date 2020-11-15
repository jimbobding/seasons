from django.shortcuts import render
from .models import Subscriptions


def subscriptions(request):
    """ A view to the subscriptions page  """

    subscriptions = Subscriptions.objects.all()
    context = {
        'subscriptions': subscriptions,
    }

    return render(request, "subscriptions/subscriptions.html", context)

