from django.shortcuts import render, get_object_or_404

from .models import Boxes, Season


# Create your views here.
def all_boxes(request):
    """ A view to show all boxes including sorting and searching quries  """

    boxes = Boxes.objects.all()
    season = Season.objects.all()

    context = {
        'boxes': boxes,
        'season': season
    }

    return render(request, "boxes/boxes.html", context)


def season_detail(request, season_id):
    """ A view to showing each season individulaly """

    season = get_object_or_404(Season, pk=season_id)

    context = {
        'season': season
    }

    return render(request, "boxes/season_detail.html", context)