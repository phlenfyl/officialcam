from django.views.generic import ListView
from django.shortcuts import get_object_or_404
from django.http import HttpResponse

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import serializers, status, generics

from .models import *
from main.serializers import AuthorSerializer, SermonSerializer

# Create your views here.

def audioDownload(request, id):
    song = get_object_or_404(Sermon, pk = id)
    file_path = song.audio.path

    with open(file_path, 'rb') as file:
        response = HttpResponse(file.read(), content_type = 'audio/mpeg')
        response['Content-Desposition'] = 'attachment; filename="{}"'.format(song.audio.name)
        print(response)
        return response


class SermonListView(ListView):
    model = Sermon
    template_name = 'pages/sermon.html'
    paginate_by = 2

class AuthorListAndCreateView(APIView):
    
    def post(self, request):
        serializer = AuthorSerializer(data = request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response({"msg": "already existed"}, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
       author = Author.objects.all()
       serializer = AuthorSerializer(author, many= True)
       return Response(serializer.data, status=status.HTTP_200_OK)
       

class SermonListAndCreateView(APIView):
    
    def post(self, request):
        serializer = SermonSerializer(data = request.data, context ={'request': request})

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
       sermon = Sermon.objects.all()
       serializer = SermonSerializer(sermon, many= True, context ={'request': request})
       return Response(serializer.data, status=status.HTTP_200_OK)
       
    


class SermonRUDView(APIView):

    def get(self, request, slug):
        try:
            query_set = Sermon.objects.get(slug=slug)
        except Sermon.DoesNotExist:
            return Response(status= status.HTTP_404_NOT_FOUND)

        serializer = SermonSerializer(query_set, many=False)

        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def put(self, request, slug):
        try:
            query_Set = Sermon.objects.get(slug=slug)
        except Sermon.DoesNotExist:
           return Response(status= status.HTTP_404_NOT_FOUND)

        serializer = SermonSerializer(query_Set, data= request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_205_RESET_CONTENT)

        return Response(serializer.errors, status = status.HTTP_405_BAD_REQUEST)

    def patch(self, request, slug):
        try:
            query_Set = Sermon.objects.get(slug=slug)
        except Sermon.DoesNotExist:
           return Response(status= status.HTTP_404_NOT_FOUND)

        serializer = SermonSerializer(query_Set, data= request.data, partial = True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_205_RESET_CONTENT)

        return Response(serializer.errors, status = status.HTTP_405_BAD_REQUEST)
    
    def delete(self, request, slug):
        try:
            query_Set = Sermon.objects.get(slug=slug)
        except Sermon.DoesNotExist:
           return Response(status= status.HTTP_404_NOT_FOUND)
        
        query_Set.delete()
        return Response({"msg":"Successfully deleted"}, status = status.HTTP_204_NO_CONTENT)


