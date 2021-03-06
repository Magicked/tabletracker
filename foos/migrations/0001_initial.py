# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-23 19:47
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DoublesGame',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('team1_score', models.IntegerField(default=0)),
                ('team2_score', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('player_name', models.CharField(max_length=100)),
                ('singles_wins', models.IntegerField(default=0)),
                ('singles_losses', models.IntegerField(default=0)),
                ('doubles_wins', models.IntegerField(default=0)),
                ('doubles_losses', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='SinglesGame',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('player1_score', models.IntegerField(default=0)),
                ('player2_score', models.IntegerField(default=0)),
                ('player1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='singles_team1', to='foos.Player')),
                ('player2', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='singles_team2', to='foos.Player')),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('player1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='team_player1', to='foos.Player')),
                ('player2', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='team_player2', to='foos.Player')),
            ],
        ),
        migrations.AddField(
            model_name='doublesgame',
            name='team1',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='doubles_team1', to='foos.Team'),
        ),
        migrations.AddField(
            model_name='doublesgame',
            name='team2',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='doubles_team2', to='foos.Team'),
        ),
    ]
