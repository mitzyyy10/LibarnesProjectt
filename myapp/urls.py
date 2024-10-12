from django.urls import path
from . import views
from .views import AboutView, HomeView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('about/', AboutView.as_view(), name='about'),
]
