from django.http import HttpResponse
from epcis_event_hash_generator import hash_generator

def hash(request):
    eventJson = request.body
    (hashes, prehashes) = hash_generator.epcis_hash_from_json(eventJson)
    return HttpResponse(",".join(hashes))
