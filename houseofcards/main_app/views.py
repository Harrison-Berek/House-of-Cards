from django.shortcuts import render
# from django.http import HttpResponse

# Create your views here.
def home(request):
  return render(request, 'home.html')

def games_index(request):
  return render(request, 'games/index.html', {
    'games': games 
    })

# def favorites_index(request):
#   return render(request, 'favorites/index.html', {
    
#   } )
