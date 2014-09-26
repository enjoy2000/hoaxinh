'''
Created on Apr 13, 2014

@author: antipro
'''
from django.contrib import admin
from accounts import models
from awesome_avatar.fields import AvatarField
from awesome_avatar.widgets import AvatarWidget

class UserProfileAdmin(admin.ModelAdmin):

    list_display = ('id', 'user', 'avatar')
    list_editable = ()

    formfield_overrides = {
        AvatarField: {'widget': AvatarWidget},
    }

    search_fields = ['user__id', 'user__username', 'user__last_name', 'user__first_name']

    list_display_links = ('user',)

    actions_on_top = True
    actions_on_bottom = True


admin.site.register(models.UserProfile, UserProfileAdmin)
