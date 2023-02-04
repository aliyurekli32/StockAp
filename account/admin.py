from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from django.contrib.auth.models import User


# class UserAdminWithGroup(UserAdmin):
#     def group_name(self, obj):
#         queryset = obj.groups.values_list('name', flat=True)
#         groups = []
#         for group in queryset:
#             groups.append(group)

#         return ' '.join(groups)

#     list_display = UserAdmin.list_display + ('group_name',)


# admin.site.unregister(User)
# admin.site.register(User, UserAdminWithGroup)
