from django.shortcuts import render
from . models import Team , Player , Matches , Points
from django.http import HttpResponse
import random


def home(request):

    """ This is home page for displaying menu of application 
    return menu of the application """

    return render(request, 'home.html' )

def team_list(request):

    """This method is for displaying team list 
    return team lists which is present in our database """
    try:
        teams = Team.objects.all()
        return render(request, 'teamlist.html',{'teams':teams} )
    
    except Exception as e:
        return HttpResponse(e)

def team_detail(request, team_id):

    """ This method is for displaying all players which belongs to a particular team 
    accept team id and return all players of team """
    try:
        team = Team.objects.get(pk=team_id)
        players = Player.objects.filter(team_id_id = team_id)
        return render(request, 'teamdetail.html', {'players':players,'team':team})

    except Team.DoesNotExist:
        context = {}
        context['error_message'] = ("\n Team id is not valid.")
        return render(request, 'teamdetail.html', context)

    except Exception as e:
        return HttpResponse(e)


def player_list(request):

    """This method is for return all players which are present in our database """
    try:
        players = Player.objects.all()
        return render (request, 'playerlist.html', {'players':players} )

    except Exception as e:
        return HttpResponse(e)


def conduct_match(request):

    """This method is used to conduct a match between teams which are present in our database
     and also display result of match which team has won the match """

    if request.method == "GET":
        return render(request, 'conductmatch.html')

    else:
        context = {}
        err_msg = ("Match number cannot be negative")
        try:
            team_1_name = request.POST['team_1']
            team_2_name = request.POST['team_2']
            match_number = request.POST['match_number']
            if int(match_number) < 1:
                raise KeyError
            match_stadium = request.POST['match_stadium']
            match_location = request.POST['match_location']
        except KeyError:
            context['error_message'] = err_msg
            return render(request, 'conductmatch.html', context)
        else:

            try:
                team_1 = Team.objects.get(name__exact=team_1_name)
                team_2 = Team.objects.get(name__exact=team_2_name)
                match = Matches(match_id=match_number, stadium=match_stadium,location=match_location)
                match.save()
                match.teams.set([team_1, team_2])
                winner_team = random.choice([team_1_name,team_2_name])
                match.winner = winner_team
                match.save()

            except Team.DoesNotExist:
                context['error_message'] = ("\n Entered team is not present in our database . Please "
                                            "try again with valid teams.")
                return render(request, 'conductmatch.html', context)

            return render(request, 'conductmatch.html', context)
        
def match_results(request):

    """This method is used to display Match result """
    try:
        matches = Matches.objects.all()
        return render(request,'result.html',{'matches':matches})

    except Exception as e:
        return HttpResponse(e)


def team_points(request):
    """This method is used to display Team points """
    try:
        points = Points.objects.all()
        return render(request,'teampoints.html', {'points':points})

    except Exception as e:
        return HttpResponse(e)


