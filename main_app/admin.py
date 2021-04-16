from django.contrib import admin
from .models import Game, Comment, Badge

# Register your models here.
admin.site.register(Game)
admin.site.register(Comment)
admin.site.register(Badge)