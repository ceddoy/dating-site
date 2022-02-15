from django.contrib import admin

from matchapp.models import Like


class LikeAdmin(admin.ModelAdmin):
    list_display = ('from_like_user', 'to_like_user')


admin.site.register(Like, LikeAdmin)
