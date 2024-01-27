from django.shortcuts import render
from django.views.generic import View
# Create your views here.

class LobbyView(View):
     def get(self,request):
          return render(template_name='chat/lobby.html', request=request)