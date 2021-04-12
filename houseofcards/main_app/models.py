from django.db import models
from django.urls import reverse

# Create your models here.
class Game(models.Model):
  name = models.CharField(max_length=100)
  cards_used = models.CharField(max_length=100)
  rules = models.TextField(max_length=5000)
  region = models.CharField(max_length=100)
  num_player_choices = (
    ("1", "1"),
    ("2", "2"),
    ("3", "3"),
    ("4", "4"),
    ("5", "5+"),
  )
  num_players = models.CharField(
    max_length= 20,
    choices = num_player_choices,
    default=1,
    )
  created = models.DateTimeField(auto_now_add=True)
  updated = models.DateTimeField(auto_now=True)

  def __str__(self):
    return self.name

  def get_absolute_url(self):
    return reverse('index')
