from django.shortcuts import render
# from django.http import HttpResponse

class Games:  # Note that parens are optional if not inheriting from another class
  def __init__(self, name):
    self.name = name

games = [
  Games('Spades'),
]

# Create your views here.
def home(request):
    return render(request, 'home.html')

def games_index(request):
    return render(request, 'games/index.html', {
        'games': games 
    })