from django.contrib import admin
from . import models
# Register your models here.

class GroupMemberInline(admin.TabularInline):
    '''Tabular Inline View for Groupmembers'''

    model = models.GroupMember

admin.site.register(models.Group)
