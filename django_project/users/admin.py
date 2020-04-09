from django.contrib import admin
from django.contrib.auth.models import Group
from fight_service.models import Fighter, FighterLink, TeamMember, TeamMemberLink,FightCards

import os


admin.site.site_header = 'Wieczór Walk - Panel Administracyjny'





class FighterLinksForAdmin(admin.StackedInline):
    model = FighterLink
    extra = 0

class TeamMemberLinksForAdmin(admin.StackedInline):
    model = TeamMemberLink
    extra = 0



class FighterInstanceAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Podstawowe',          {'fields':['name','surname','birth','sex','image']}),
        ('Dane zawodnika', {'fields':['weight','category','has_belt','wins','losts','draws','description']}),
        ('Publikacja', {'fields':['priority','published']})
    ]

    inlines = [FighterLinksForAdmin]


class TeamMemberInstanceAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Podstawowe',          {'fields':['name','surname', 'role', 'image', 'description']}),
        ('Publikacja', {'fields':['priority','published']})
    ]

    inlines = [TeamMemberLinksForAdmin]


class FightInstanceAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Podstawowe',          {'fields':['image','category', 'main_event', 'description']}),
        ('Publikacja', {'fields':['priority','set_hidden', 'published']})
    ]



admin.site.register(FightCards, FightInstanceAdmin)
admin.site.register(TeamMember, TeamMemberInstanceAdmin)
admin.site.register(Fighter, FighterInstanceAdmin)
admin.site.unregister(Group)