from django.contrib import admin
from .models import Player, Match


@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):
    list_display = ('nickname', 'full_name', 'role', 'is_active', 'order')
    list_editable = ('order', 'is_active')
    list_filter = ('role', 'is_active')
    search_fields = ('nickname', 'full_name')


@admin.register(Match)
class MatchAdmin(admin.ModelAdmin):
    list_display = ('opponent', 'tournament', 'date', 'result', 'score')
    list_filter = ('result',)
    ordering = ('-date',)
