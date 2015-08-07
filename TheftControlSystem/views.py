from django.shortcuts import render_to_response
from django.template import RequestContext

from apps.VictimMap.models import Victim, Place
from django.db.models import Count


def home(request):
    places = Place.objects.annotate(num_victim=Count('victim'))
    print places
    print [i.num_victim for i in places]
    parameters = RequestContext(request)
    parameters['places'] = places
    return render_to_response('home.html', parameters)
