from django.urls import path
from .views import (SnackListView,SnackDetailView,SnackCreateView,SnackDeleteView,SnackUpdateView,
)
urlpatterns = [
    path('',SnackListView.as_view(),name='snack_list'),
    
]