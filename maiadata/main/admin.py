from django.contrib import admin
from .models import Data


@admin.register(Data)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('espid', 'topic','timestamp','peso','temperatura','umidita')
