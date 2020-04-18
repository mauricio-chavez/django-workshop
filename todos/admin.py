"""Admin site for TODOs app"""

from django.contrib import admin


from .models import Todo

admin.site.register(Todo)
