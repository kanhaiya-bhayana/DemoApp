from django.urls import path
from . import views

urlpatterns = [
    path('', views.index,name='home-page'),
    path('about/', views.about,name='about-page'),
    path('python/', views.python,name='python'),
    path('remove_punc/', views.remove_punc,name='remove_punc'),
    path('result_rem_punc/', views.result_rem_punc,name='result_rem_punc'),
]