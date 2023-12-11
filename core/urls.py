from django.urls import path
from . import views

urlpatterns = [
    path('ngram/', views.ngram_view, name='ngram_form'),
]