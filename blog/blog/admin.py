from django.contrib import admin

# Register your models here.
from .models import Post
admin.site.register(Post) # register the model with django's admin interface for mgt