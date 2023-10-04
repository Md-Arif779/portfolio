from django.contrib import admin
from .models import Contact, Profile, About, Skill

# Register your models here.


@admin.register(Contact)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'timestamp')

admin.site.register(Profile)
admin.site.register(About)
admin.site.register(Skill)