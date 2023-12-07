from django.urls import path

from .views import *

app_name ='program'


urlpatterns = [
    path('', ProgramList.as_view(), name= 'program'),


    path('create/', CreateProgramView.as_view(), name= 'create-program'),
    path('all/', ProgramListView.as_view(), name= 'view-all-program'),
    path('rud/<str:slug>/', ProgramDetailView.as_view(), name= 'view-program'),
]