
from django.urls import path
from test_app import views

app_name='test_app'

urlpatterns=[
    path('',views.Home,name='Add'),
    path('latest/',views.latest,name='latest'),
    path('sports/',views.sports,name='sports'),
    path('entertain/',views.Entertainment,name='entertain'),
    path('polity/',views.Politics,name='polity'),
    path('latestselect/',views.LatestSelect,name='latestselect'),
    path('sportsselct/',views.SportSelect,name='sportsselect'),
    path('entertainselect/', views.EntertainSelect, name='entertainselect'),
    path('polityselect/', views.PolitySelect, name='polityselect')
]
