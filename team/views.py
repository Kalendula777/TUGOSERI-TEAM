from django.shortcuts import render, get_object_or_404
from .models import Player, Match


def home(request):
    players = Player.objects.filter(is_active=True)
    upcoming_matches = Match.objects.filter(result='upcoming')[:5]
    context = {
        'players': players,
        'matches': upcoming_matches,
    }
    return render(request, 'team/home.html', context)


def player_detail(request, pk):
    player = get_object_or_404(Player, pk=pk)
    return render(request, 'team/player_detail.html', {'player': player})


def matches(request):
    all_matches = Match.objects.all()
    return render(request, 'team/matches.html', {'matches': all_matches})
