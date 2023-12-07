from django.urls import path

from .views import *

app_name ='main'


urlpatterns = [
    
    path('', index, name= 'index'),
    path('mfmcam/', mfmcam, name= 'mfmcam'),
    path('contact/', contact, name= 'contact'),
    path('api/overview', ApiOverview, name= 'home'),
    
    path('limited/main/', LimitedMainView.as_view(), name= 'landing-m'),
    path('limited/sermon/', LimitedSermonView.as_view(), name= 'landing-s'),
    path('limited/program/', LimitedProgramView.as_view(), name= 'landing-p'),
    path('weekcl/', WeeklyListAndCreateView.as_view(), name= 'weekcl'),
    path('rud/<str:slug>/', WeeklyRUDView.as_view(), name= 'rud'),

]