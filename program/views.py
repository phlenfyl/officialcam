from django.views.generic import ListView, View
from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import serializers, status, generics

# from django.http import HttpResponse

from .models import *
from main.views import G
# from .forms import *
from main.serializers import ProgramSerializer

# Create your views here.


class ProgramList(View):
    template_name = 'pages/program.html'
    prog = G.prog.filter(display=True)
    week = G.week.filter(display = True)

    def get(self, request):
        prog = self.prog
        week = self.week

        print(prog)

        return render (request, self.template_name, {'program': prog, "weekly":week})

# class ProgramView(ListView):
#     model = Program
#     template_name = 'pages/program.html'
#     queryset = G.prog.filter(display=True)
    # url = request.META.get('HTTP_REFERER')

    # def get_queryset(self):

    #     program_filters = {
    #         'speicalprogram': {'speicalprogram': True},
    #         'deliverance': {'deliverance': True},
    #         'counseling': {'counseling': True},
    #     }

    #     program = self.request.query_params.get('program')

    #     if program in program_filters:
    #         return self.queryset.filter(**program_filters['program'])
    #     else:
    #         return "/"
        



class ProgramListView(generics.ListAPIView):
    serializer_class = ProgramSerializer
    queryset = Program.objects.filter(display=True)
    # filter_backends = [OrderingFilter]
    # ordering_fields = ['id']  # You can order by any field you want

    def get_queryset(self):
        # Define a dictionary to map categories to their respective filters
        program_filters = {
            'speicalprogram': {'speicalprogram': True},
            'deliverance': {'deliverance': True},
            'counseling': {'counseling': True},
        }

        # Get the program from the URL parameter
        program = self.request.query_params.get('program')

        # Check if the program is valid and filter accordingly
        if program in program_filters:
            return self.queryset.filter(**program_filters[program])
        else:
            return Program.objects.filter(display= True)  # Return an empty queryset for invalid categories


class ProgramDetailView(APIView):

    def get(self, request,slug):
        try:
            query_set = Program.objects.get(slug=slug)
        except Program.DoesNotExist:
            return Response(status= status.HTTP_404_NOT_FOUND)

        serializer = ProgramSerializer(query_set, many=False)

        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def put(self, request, slug):
        try:
            query_Set = Program.objects.get(slug=slug)
        except Program.DoesNotExist:
           return Response(status= status.HTTP_404_NOT_FOUND)

        serializer = ProgramSerializer(query_Set, data= request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_205_RESET_CONTENT)

        return Response(serializer.errors, status = status.HTTP_405_BAD_REQUEST)

    def patch(self, request, slug):
        try:
            query_Set = Program.objects.get(slug=slug)
        except Program.DoesNotExist:
           return Response(status= status.HTTP_404_NOT_FOUND)

        serializer = ProgramSerializer(query_Set, data= request.data, partial = True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_205_RESET_CONTENT)

        return Response(serializer.errors, status = status.HTTP_405_BAD_REQUEST)
    
    def delete(self, request, slug):
        try:
            query_Set = Program.objects.get(slug=slug)
        except Program.DoesNotExist:
           return Response(status= status.HTTP_404_NOT_FOUND)
        
        query_Set.delete()
        return Response({"msg":"Successfully deleted"}, status = status.HTTP_204_NO_CONTENT)
        

class CreateProgramView(generics.CreateAPIView):

    serializer_class = ProgramSerializer

    def get_queryset(self):
        return Program.objects.all()









