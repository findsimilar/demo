from rest_framework import serializers
from .models import Example


class ExampleSerializer(serializers.ModelSerializer):
    text = serializers.StringRelatedField()
    texts = serializers.StringRelatedField(many=True)

    class Meta:
        model = Example
        fields = ('name', 'text', 'texts')


class ExampleNameSerializer(serializers.ModelSerializer):

    class Meta:
        model = Example
        fields = ('name',)
