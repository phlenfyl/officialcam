from django.urls import path

from .views import *

app_name ='sermon'


urlpatterns = [
    path('download/<str:id>/', audioDownload, name= 'download'),
    path('', SermonListView.as_view(), name= 'sermon'),


    
    path('authorcl/', AuthorListAndCreateView.as_view(), name= 'authorcl'),
    path('sermoncl/', SermonListAndCreateView.as_view(), name= 'sermoncl'),
    path('rud/<str:slug>/', SermonRUDView.as_view(), name= 'rud'),
]