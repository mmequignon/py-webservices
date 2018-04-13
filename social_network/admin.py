from django.contrib import admin
from .models import Buddy, BuddyExtension, Content, Comment, Post, Feeling


admin.site.register(Buddy)
admin.site.register(BuddyExtension)
admin.site.register(Content)
admin.site.register(Comment)
admin.site.register(Post)
admin.site.register(Feeling)
