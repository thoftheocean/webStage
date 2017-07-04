from rest_framework import serializers
from djangorestframework.models import Poem

class PoemSerializer(serializers.ModelSerializer):
    class Meta:
        model =Poem
        fields =['author', 'title', 'type']