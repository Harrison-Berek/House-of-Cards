from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Game
# from django.http import HttpResponse

# Create your views here.
def home(request):
  return render(request, 'home.html')

def games_index(request):
  games = Game.objects.all()
  return render(request, 'games/index.html', {
    'games': games 
    })

class GamesCreate(CreateView):
  model = Game
  fields = '__all__'


# def favorites_index(request):
#   return render(request, 'favorites/index.html', {
    
#   } )
