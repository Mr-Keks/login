from django.forms import ModelForm

from .models import login_form

class loginForm(ModelForm):
	class Meta:
		model = login_form
		fields = ('login', 'password')