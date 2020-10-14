from django.http import HttpResponse
from epcis_event_hash_generator import hash_generator

import logging

def hash(request):

    if request.content_type == 'application/json':
        epcisJsonDoc = request.body
        (hashes, prehashes) = hash_generator.epcis_hash_from_json(epcisJsonDoc)
        return HttpResponse(",".join(hashes))
    elif request.content_type == 'application/xml':
        epcisXmlDoc = request.body
        (hashes, prehashes) = hash_generator.epcis_hash_from_xml(epcisXmlDoc)
        return HttpResponse(",".join(hashes))
    else:
        return HttpResponse.BadRequest
