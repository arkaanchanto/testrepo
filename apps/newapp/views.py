from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import mode


@api_view(http_method_names=["GET"])
def myview(request):
    v = mode.objects.create(a="abc")
    v.save()

    return Response({"message": "abcd"}, status=status.HTTP_200_OK)
