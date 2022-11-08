from rest_framework.response import Response
from rest_framework.decorators import api_view

import requests
import xmltodict as xmltodict
import json


@api_view(['GET'])
def ursafe(request):
    if request.method == "GET":
        apiUrl = 'https://www.maniadb.com/api/search/metallica/?sr=artist&display=10&key=example&v=0.5'

        req = requests.get(apiUrl)

        xpars = xmltodict.parse(req.text)

        jsonDump = json.dumps(xpars)

        jsonBody = json.loads(jsonDump)
        return Response(jsonBody)
