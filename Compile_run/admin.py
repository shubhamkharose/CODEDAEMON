from django.contrib import admin
from .models import User_Problem,TestCase,Problem_session,AdminSettings

# Register your models here.

admin.site.register(Problem_session)
admin.site.register(TestCase)
class UserProblemAdmin(admin.ModelAdmin):
	list_display = ("Problem","User","status","score")
admin.site.register(User_Problem,UserProblemAdmin)
admin.site.register(AdminSettings)
