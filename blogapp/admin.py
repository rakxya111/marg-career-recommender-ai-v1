from django.contrib import admin
from .models import Tag , Post , Comment , Contact, Newletter

admin.site.register(Tag)
admin.site.register(Comment)
admin.site.register(Contact)
admin.site.register(Post)