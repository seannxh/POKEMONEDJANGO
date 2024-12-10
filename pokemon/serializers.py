from .models import Pokemon
from rest_framework import serializers
from django.contrib.auth.models import User

class PokemonSerializers(serializers.HyperlinkedModelSerializer):
    user=serializers.ReadOnlyField(source='user.username')
    class Meta: 
        model=Pokemon
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ["username", "password"]  # Corrected the typo here

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
        )
        return user
