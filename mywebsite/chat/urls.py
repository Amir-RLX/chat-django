from django.urls import path
from . import views


urlpatterns = [
     path('', view=views.LobbyView.as_view())
]