from django.http.response import Http404
from .models import Music 
from .serializers import MusicSerializer
from rest_framework.views import APIView
from rest_framework.response import Response 
from rest_framework import status 

# Create your views here.

class MusicList(APIView):

    def get(self, request):
        music = Music.objects.all()
        serializer = MusicSerializer(music, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = MusicSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class MusicDetail(APIView):

    def get_object(self, pk):
        try:
            return Music.objects.get(pk=pk)
        except Music.DoesNotExist:
            raise Http404

    #get by id
    def get(self, request, pk):
        song = self.get_object(pk)
        serializer = MusicSerializer(song)
        return Response(serializer.data)
