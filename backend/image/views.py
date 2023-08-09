from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.views import APIView
from utils.ai import send_req
from uuid import uuid1

class AiSendView(APIView):
    """
    A view that can accept POST requests with JSON content.
    """
    parser_classes = [JSONParser]

    def post(self, request, format=None):
        imgdata = request.data["img"]
        filename = uuid1()
        res = send_req("127.0.0.1", imgdata, filename)
        return Response({'result': res["result"]})