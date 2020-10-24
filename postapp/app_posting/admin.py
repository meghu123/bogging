from django.contrib import admin
from .models import Post,comment,Tags


# Register your models here.


class postAdmin(admin.ModelAdmin):
    list_display = ['Create_by','title','description']

admin.site.register(Post,postAdmin)



class commentAdmin(admin.ModelAdmin):
    list_display = ['user','post','content','time']

admin.site.register(comment,commentAdmin)


class TagAdmin(admin.ModelAdmin):
    list_display = ['tag_name']

admin.site.register(Tags,TagAdmin)
