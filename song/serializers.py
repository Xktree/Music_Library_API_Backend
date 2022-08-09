from rest_framework import serializers
from .models import Song 

class MusicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song 
        fields = ['title', 'artist', 'album', 'genre', 'release_date']