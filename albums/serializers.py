from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import Album
from users.serializers import UserSerializer


class AlbumSerializer(serializers.ModelSerializer):
    # user = UserSerializer(read_only=True)

    class Meta:
        model = Album

        fields = [
            'id',
            'name',
            'year',
            'user_id',
        ]

        read_only_fields = [
            'user_id'
        ]
        
        # extra_kwargs = {
        #     'year': {'required': True},
        #     'name': {'required': True}
        # }

    # def create(self, validated_data):
    #     return Album.objects.create(**validated_data)

    # id = serializers.IntegerField(read_only=True)
    # name = serializers.CharField(max_length=255)
    # year = serializers.IntegerField()
    # user_id = serializers.IntegerField(read_only=True)