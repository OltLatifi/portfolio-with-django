from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import skills, languages, technologies, projects
from captcha.fields import ReCaptchaField
from captcha.widgets import ReCaptchaV3


class language_f(forms.ModelForm):
	class Meta:
		model = languages
		
		fields = ['Text']


class technology_f(forms.ModelForm):
	class Meta:
		model = technologies
		
		fields = ['Language','Text']
		# label = {'language':'Language','Text':'Text'}


class projects_f(forms.ModelForm):
	class Meta:
		model = projects
		
		fields = ['Text','Link','Description']




class contact_f(forms.Form):

	captcha = ReCaptchaField(
		widget=ReCaptchaV3(
			attrs={
				'required_score':0.85,
			}
		)
	)