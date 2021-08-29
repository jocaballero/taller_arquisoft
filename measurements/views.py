from .logic.logic_measurements import *
from django.core import serializers
from django.http import HttpResponse

def get_measurements(request):
    variables = get_all_measurements()
    variable_list = serializers.serialize('json', variables)
    return HttpResponse(variable_list, content_type='application/json')

def get_measurements_id(request, id):
    variable = get_measurement(id)
    variable_json = serializers.serialize('json', variable)
    return HttpResponse(variable_json, content_type='application/json')