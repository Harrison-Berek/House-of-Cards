# Generated by Django 3.2 on 2021-04-12 22:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_game_num_players'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='num_players',
            field=models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5+')], default=1, max_length=20),
        ),
    ]
