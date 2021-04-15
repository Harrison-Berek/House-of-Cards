from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Game, Comment
from .forms import CommentForm


# Create your views here.
def home(request):
  return render(request, 'home.html')

def games_index(request):
  games = Game.objects.all()
  return render(request, 'games/index.html', {
    'games': games 
    })

def games_details(request, game_id):
  game = Game.objects.get(id=game_id)
  comment_form = CommentForm()   
  return render(request, 'games/details.html', {
    'game' : game,
    'comment_form': comment_form
  })

def comments_create(request, game_id):
  form = CommentForm(request.POST)
  if form.is_valid():
    new_comment = form.save(commit=False)
    new_comment.game_id = game_id
    new_comment.save()
  return redirect('details', game_id=game_id)

# def comments_update(request, comment_id):
#   comment = Comment.objects.get(id=comment_id)

  

class GamesCreate(CreateView):
  model = Game
  fields = '__all__'

class GamesUpdate(UpdateView):
  model = Game
  fields = ['rules', 'num_players', 'cards_used', 'region']

class GamesDelete(DeleteView):
  model = Game
  success_url = '/games/'

class CommentsDelete(DeleteView):
  model = Comment
  success_url = '/games/'



