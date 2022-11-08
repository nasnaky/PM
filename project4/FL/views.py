from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.decorators import api_view

import requests
import xmltodict as xmltodict
import json


@api_view(['POST'])
def ursafe(request):
    if request.method == "POST":
        data = JSONParser().parse(request)
        url = data['url']

        req = requests.get(url)

        xpars = xmltodict.parse(req.text)

        jsonDump = json.dumps(xpars)

        jsonBody = json.loads(jsonDump)
        return Response(jsonBody)
