from django.shortcuts import render

from .models import Box

# Create your views here.
def all_boxes(request):
    """ A view to show all products including sorting and searching quries  """

    boxes = Box.objects.all()

    context = {
        'boxes': boxes
    }

    return render(request, "boxes/boxes.html", context)