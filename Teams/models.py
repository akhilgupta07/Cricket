from django.db import models

# Create your models here.
class Team(models.Model):
    """ Model class for Teams details   """

    team_id = models.IntegerField (primary_key=True)
    name = models.CharField (max_length=200)
    logo_uri = models.ImageField (upload_to='pics')
    club_state = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Player(models.Model):
    """ Model class for Player details   """
    
    player_id = models.IntegerField (primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    image_uri = models.ImageField(upload_to='pics')
    jersey_number = models.PositiveIntegerField()
    country = models.CharField(max_length=100)
    team_id = models.ForeignKey(Team,on_delete = models.CASCADE) 


class Matches(models.Model):

    """ Model class for Match Details """

    match_id = models.IntegerField(primary_key=True)
    teams = models.ManyToManyField(Team)
    stadium = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    winner = models.CharField(max_length=200)
    date = models.DateTimeField(auto_now=True)


class PlayerHistory(models.Model):

    """ Model class for Player performance record  """
    
    id = models.IntegerField (primary_key=True)
    player_id = models.ForeignKey(Player, on_delete=models.CASCADE)
    no_of_matches = models.PositiveIntegerField()
    total_run = models.PositiveIntegerField()
    highest_score = models.PositiveIntegerField()
    no_of_fifties = models.PositiveIntegerField()
    no_of_hundreds = models.PositiveIntegerField()


class Points(models.Model):

    """Model class for Team Points"""
    
    id = models.IntegerField(primary_key=True)
    team = models.OneToOneField(Team, on_delete=models.CASCADE)
    points = models.PositiveIntegerField()
    



    



    