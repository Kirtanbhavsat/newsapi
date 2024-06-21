from django.urls import path
from .import views

urlpatterns = [
    path('',views.indexpage),
    path('news',views.newspage),
    path('sport',views.sportspage),
    path('technology',views.technologypage),
    path('politics',views.politicspage),
    path('automobile',views.automobilepage),
    path('business',views.businesspage),
    path('science',views.sicencepage),
    path('allnews',views.allnewspage),
    path('searchapi',views.searchapi),
]