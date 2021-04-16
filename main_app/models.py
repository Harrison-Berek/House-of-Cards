from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
 
num_player_choices = (
  ("1", "1"),
  ("2", "2"),
  ("3", "3"),
  ("4", "4"),
  ("5", "5+"),
)

class Badge(models.Model):
  title = models.CharField(max_length=50)
  url = models.CharField(max_length=200)

  def __str__(self):
    return self.title

  def get_absolute_url(self):
    return reverse('detail', kwargs={'game_id': self.game_id})

class Game(models.Model):
  name = models.CharField(max_length=100)
  cards_used = models.CharField(max_length=100)
  rules = models.TextField(max_length=5000)
  region = models.CharField(max_length=100)
  num_players = models.CharField(
    max_length= 20,
    choices = num_player_choices,
    default=1,
    )
  created = models.DateField(auto_now_add=True)
  updated = models.DateField(auto_now=True)
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  badges = models.ManyToManyField(Badge)


  def __str__(self):
    return self.name

  def get_absolute_url(self):
    return reverse('index')

class Comment(models.Model):
  content = models.TextField(max_length=500)
  created = models.DateField(auto_now_add=True)
  game = models.ForeignKey(Game, on_delete=models.CASCADE)

  def __str__(self):
    return self.content

  class Meta:
    ordering = ['-id']


  