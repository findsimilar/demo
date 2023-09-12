from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import RetrieveModelMixin
from .serializers import ExampleSerializer
from .models import Example


class ExampleViewSet(RetrieveModelMixin, GenericViewSet):
    serializer_class = ExampleSerializer
    queryset = Example.objects.all()
    lookup_field = 'name'
