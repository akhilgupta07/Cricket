from django.contrib import admin
from django.urls import path,include
from . import views

""" URLS for Teams app"""

urlpatterns = [
    path('',views.home ,name='home'),
    path('teamlist/', views.team_list , name ='team_list'),
    path('teamlist/<int:team_id>', views.team_detail , name ='team_detail'),
    path('playerlist/',views.player_list , name = 'player_list'),
    path('conductmatch/',views.conduct_match , name = 'conduct_match'),
    path('result/', views.match_results, name ='result'),
    path('teampoints/',views.team_points , name = 'team_points')

]
