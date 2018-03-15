from django.contrib import admin
from .models import User,AdminUser
admin.site.register(User)
admin.site.register(AdminUser)
