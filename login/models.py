from django.db import models

class login_form(models.Model):
	login = models.CharField(max_length = 100)
	password = models.CharField(max_length = 100)

	class Meta:
		verbose_name_plural = 'values'
		verbose_name_plural = 'value'
		
