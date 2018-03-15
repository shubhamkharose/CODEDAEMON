from django.contrib import admin
from .models import Contest,Problem,Con_signup,Contact

class ContestAdmin(admin.ModelAdmin):
	list_display = ("con_name","start_time","end_time")
admin.site.register(Contest,ContestAdmin),

class ProblemAdmin(admin.ModelAdmin):
	list_display = ("Contest","p_name","score","s_rate")
admin.site.register(Problem,ProblemAdmin),

class ConSignAdmin(admin.ModelAdmin):
	list_display = ("contest","user","status")
admin.site.register(Con_signup,ConSignAdmin),

admin.site.register(Contact),