from django.contrib import admin
from .models import Feedback
from .models import Post,Comment
# Register your models here.
admin.site.register(Feedback)
admin.site.register(Post)
admin.site.register(Comment)