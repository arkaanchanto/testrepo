from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


@api_view(http_method_names=["GET"])
def myview(request):
    return Response({"message": "abcd"}, status=status.HTTP_200_OK)
