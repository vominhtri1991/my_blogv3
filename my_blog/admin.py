from django.contrib import admin
from .models import Blog, PostType, Message

class MessageAdmin(admin.ModelAdmin):
	readonly_fields=('created',)

admin.site.register(Blog)
admin.site.register(PostType)
admin.site.register(Message,MessageAdmin)

# Register your models here.
