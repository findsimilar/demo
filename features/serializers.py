from rest_framework import serializers
from rest_framework.serializers import ValidationError
from find_similar import find_similar
from find_similar.calc_models import LanguageNotFoundException


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
        try:
            return find_similar(**validated_data)
        except LanguageNotFoundException as exc:
            language = validated_data.get('language')
            raise ValidationError({
                'language': f'"{language}" is not supported'
            }) from exc
