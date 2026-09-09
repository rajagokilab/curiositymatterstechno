from django.contrib import admin
from .models import Service, PortfolioProject, TeamMember, ContactMessage, Stat, HeroContent, ValueProposition

admin.site.register(Service)
admin.site.register(PortfolioProject)
admin.site.register(TeamMember)
admin.site.register(ContactMessage)
admin.site.register(Stat)
admin.site.register(HeroContent)
admin.site.register(ValueProposition)