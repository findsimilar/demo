from rest_framework import serializers
from find_similar import find_similar


class TokenTextSerializer(serializers.Serializer):
    text = serializers.CharField(required=True)
    cos = serializers.DecimalField(allow_null=True, decimal_places=2, max_digits=3)


class FindSimilarSerializer(serializers.Serializer):
    text_to_check = serializers.CharField(required=True)
    texts = serializers.ListField()
    language = serializers.CharField(required=False)
    count = serializers.IntegerField(default=5)
    dictionary = serializers.DictField(required=False)
    remove_stopwords = serializers.BooleanField(required=False)

    def create(self, validated_data):
        return find_similar(**validated_data)