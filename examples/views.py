from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import RetrieveModelMixin, ListModelMixin
from .serializers import ExampleSerializer, ExampleNameSerializer
from .models import Example


class ExampleViewSet(RetrieveModelMixin, GenericViewSet, ListModelMixin):
    serializer_class = ExampleSerializer
    queryset = Example.objects.all()
    lookup_field = 'name'

    def get_serializer_class(self):
        action_serializers = {
            'list': ExampleNameSerializer,
            'retrieve': ExampleSerializer,
        }
        return action_serializers[self.action]
