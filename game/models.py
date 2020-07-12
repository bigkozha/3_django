from django.contrib.auth.models import User
from django.db import models


class Game(models.Model):
    number = models.IntegerField()
    is_active = models.BooleanField(default=True)
    from_number = models.IntegerField(blank=True, null=True)
    to_number = models.IntegerField(blank=True, null=True)


class Guess(models.Model):
    number = models.IntegerField()
    time = models.DateField(auto_now=False, auto_now_add=True)
    is_correct = models.BooleanField(default=False)
    game = models.ForeignKey(
        Game, on_delete=models.CASCADE, related_name='guesses')
    user = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='guess_user', null=True)
