from django.http import HttpResponse

from django.shortcuts import render_to_response
from django.template import RequestContext

import urllib
import urllib2
import json
from django.utils.encoding import smart_str

import collections
import os
import random
from .models import Victim

APP_ROOT = os.path.realpath('.')
places = ['Gwarko, Lalitpur', 'Kalimati, Kathmandu, Nepal', 'Koteshwor, Kathmandu, Nepal', 'Kirtipur, Nepal','Pasupatinath, Kathmandu','Koteshwor, Kathmandu', 'Basundhara, Kathmandu', 'Patan, Lalitpur, Nepal', 'Durbar Marg, Kathmandu', 'Sitapaila, Kathmandu']
victim_places = ['Gwarko, Lalitpur', 'Kalimati, Kathmandu, Nepal', 'Koteshwor, Kathmandu, Nepal','Gwarko, Lalitpur', 'Kalimati, Kathmandu, Nepal', 'Koteshwor, Kathmandu, Nepal','Gwarko, Lalitpur', 'Kalimati, Kathmandu, Nepal', 'Koteshwor, Kathmandu, Nepal']

def get_lat_lng(location):
    l_dict = {}
    location = urllib.quote_plus(smart_str(location))
    url = 'http://maps.googleapis.com/maps/api/geocode/json?address=%s&sensor=false' % location
    response = urllib2.urlopen(url).read()
    result = json.loads(response)
    if result['status'] == 'OK':
       l_dict['lat'] = str(result['results'][0]['geometry']['location']['lat'])
       l_dict['lng'] = str(result['results'][0]['geometry']['location']['lng'])
       return l_dict
    else:
        return ''


def convert_location_to_coordinates(request):
    data = []
    for each in places:
        return_data = get_lat_lng(each)
        placemodel = {}
        d = collections.OrderedDict()
        d['model'] = "VictimMap.Place"
        d['pk'] = places.index(each) + 1
        placemodel['latitude'] = return_data['lat']
        placemodel['longitude'] = return_data['lng']
        d['fields'] = placemodel
        data.append(d)

    primarykey = 1
    for each_place in victim_places:
        victimmodel = {}
        d = collections.OrderedDict()
        d['model'] = "VictimMap.Victim"
        d['pk'] = primarykey
        victimmodel['place'] = places.index(each_place) + 1
        d['fields'] = victimmodel
        data.append(d)
        primarykey += 1

    j = json.dumps(data, indent=4)
    objects_file = APP_ROOT + "/TheftControlSystem/apps/VictimMap/fixtures/data.json"
    f = open(objects_file, 'w')
    print >> f, j
    return HttpResponse("Converted!")

