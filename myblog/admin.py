from django.contrib import admin
from .models import myblog

class myblogInfoAdmin(admin.ModelAdmin):
	list_display=('id',)
admin.site.register(myblog,myblogInfoAdmin)
