from django.contrib import admin
from .models import Box, Task, User
from django.utils.safestring import mark_safe


class BoxAdmin(admin.ModelAdmin):

    def admin_image(self, obj):
        return mark_safe('<img src="%s"/>' % obj.img)
    admin_image.allow_tags = True

    list_display = ('name', 'admin_image')


admin.site.register(Box, BoxAdmin)
admin.site.register([Task, User])
