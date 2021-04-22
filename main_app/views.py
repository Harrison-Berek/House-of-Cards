from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Game, Comment, Badge
from .forms import CommentForm

# Create your views here.
def home(request):
  return render(request, 'home.html')

def games_index(request):
  games = Game.objects.all()
  return render(request, 'games/index.html', {
    'games': games 
    })

@login_required
def games_my_games(request):
  games = Game.objects.filter(user=request.user)
  return render(request, 'games/index.html', { 
    'games': games
  })

def games_details(request, game_id):
  game = Game.objects.get(id=game_id)
  comment_form = CommentForm()
  badges = Badge.objects.all()
  user_id = request.user
  return render(request, 'games/details.html', {
    'game' : game,
    'comment_form': comment_form,
    'badges' : badges,
    'user_id': user_id,
  })

@login_required
def comments_create(request, game_id):
  form = CommentForm(request.POST)
  if form.is_valid():
    new_comment = form.save(commit=False)
    new_comment.game_id = game_id
    new_comment.user_id = request.user.id
    new_comment.save()
  return redirect('details', game_id=game_id)

@login_required
def assoc_badge(request, game_id):
  Game.objects.get(id=game_id).badges.add(request.POST.get('badge'))
  return redirect('details', game_id=game_id)

@login_required
def unassoc_badge(request, game_id, badge_id):
  Game.objects.get(id=game_id).badges.remove(badge_id)
  user_id = request.user
  return redirect('details', game_id=game_id)

def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('index')
    else:
      error_message = 'Invalid sign up - try again'
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)

@login_required
def comments_delete(request, game_id, comment_id):
  comment = Comment.objects.get(id=comment_id)
  comment.delete()
  return redirect('details', game_id=game_id)
  
class GamesCreate(CreateView, LoginRequiredMixin):
  model = Game
  fields = ['name','rules', 'num_players', 'cards_used', 'region']
  def form_valid(self, form):
    form.instance.user = self.request.user 
    return super().form_valid(form)

class GamesUpdate(UpdateView, LoginRequiredMixin):
  model = Game
  fields = ['rules', 'num_players', 'cards_used', 'region']

class GamesDelete(DeleteView, LoginRequiredMixin):
  model = Game
  success_url = '/games/'