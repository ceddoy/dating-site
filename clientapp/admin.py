from django.contrib import admin

from clientapp.models import Client, Location


class ClientViewAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'sex')

    def save_model(self, request, obj, form, change):
        if change:
            orig_obj = Client.objects.get(pk=obj.pk)
            if obj.password != orig_obj.password:
                obj.set_password(obj.password)
            obj.save()
        else:
            obj.set_password(obj.password)
            super().save_model(request, obj, form, change)


admin.site.register(Client, ClientViewAdmin)
admin.site.register(Location)
