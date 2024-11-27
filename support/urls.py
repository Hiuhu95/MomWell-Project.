from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('ppd/', views.ppd, name='ppd'),
    path('anx/', views.anx, name='anx'),
    path('weightmgt/', views.weightmgt, name='weightmgt'),
]
