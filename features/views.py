from drf_yasg.utils import swagger_auto_schema
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import FindSimilarSerializer, TokenTextSerializer


class FindSimilarApiView(APIView):

    @swagger_auto_schema(
        operation_description="Find similar objects",
        request_body=FindSimilarSerializer,
    )
    def post(self, request, format=None):
        serializer = FindSimilarSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        result = serializer.save()
        result_serializer = TokenTextSerializer(result, many=True)
        return Response(result_serializer.data)
