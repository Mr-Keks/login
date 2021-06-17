from django.contrib import admin

from .models import login_form

class loginAdmin(admin.ModelAdmin):
	list_display = ('login', 'password')


admin.site.register(login_form)
