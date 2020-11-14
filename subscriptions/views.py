from django.shortcuts import render


def subscriptions(request):
    """ A view to the index page  """

    return render(request, "subscriptions/subscriptions.html")
