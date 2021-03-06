# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-09 20:50
from __future__ import unicode_literals

from django.db import migrations


def fix_games_played(apps, schema_editor):
    Player = apps.get_model('foos', 'Player')
    Team = apps.get_model('foos', 'Team')
    for player in Player.objects.all():
        player.singles_games_played = player.singles_wins
        player.singles_games_played += player.singles_losses
        player.singles_games_played += player.singles_draws
        player.doubles_games_played = player.doubles_wins
        player.doubles_games_played += player.doubles_losses
        player.doubles_games_played += player.doubles_draws
        player.save()

    for team in Team.objects.all():
        team.games_played = team.wins
        team.games_played += team.losses
        team.games_played += team.draws
        team.save()


class Migration(migrations.Migration):

    dependencies = [
        ('foos', '0009_auto_20170203_1741'),
    ]

    operations = [
        migrations.RunPython(fix_games_played),
    ]
