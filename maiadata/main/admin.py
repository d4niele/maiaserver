from django.contrib import admin
from .models import Data


@admin.register(Data)
class AuthorAdmin(admin.ModelAdmin):
    def has_add_permission(self, request, obj=None):
        return False
    list_filter = ('espid','topic')
    list_display = ('espid','timereg', 'topic','timestamp','peso','temperatura','umidita')
