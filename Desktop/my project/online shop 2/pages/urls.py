from django.urls import path
from .views import HomePageView,HomeUsPageView

urlpatterns = [
    path('',HomePageView.as_view(),name='home'),
    path('aboutus/',HomeUsPageView.as_view(),name='aboutus'),
]