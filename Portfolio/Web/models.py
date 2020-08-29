from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

full_stack = {('Front-end','Front-end'),
			  ('Back-end', 'Back-end'),
			  ('Game-dev', 'Game-dev')}



class skills(models.Model):
	Editor = models.ForeignKey(User, on_delete=models.CASCADE, default =1)
	Field = models.CharField(max_length = 10, choices = full_stack)
	Text = models.TextField(max_length=100)

	def __str__(self):
		return self.Text

	def get_absolute_url(self):
		return reverse('Skills', kwargs={'pk': self.pk})



class languages(models.Model):
	Editor = models.ForeignKey(User, on_delete=models.CASCADE, default =1)
	Text = models.TextField(max_length = 20)

	def __str__(self):
		return self.Text

	def get_absolute_url(self):
		return reverse('Crud-lang', kwargs={'pk': self.pk})



class technologies(models.Model):
	Editor = models.ForeignKey(User, on_delete=models.CASCADE, default =1)
	Language = models.ForeignKey(languages, on_delete = models.CASCADE)
	Text = models.TextField(max_length = 20)

	def __str__(self):
		return self.Text

	def get_absolute_url(self):
		return reverse('Crud-tech', kwargs={'pk': self.pk})


class projects(models.Model):
	Editor = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
	Text = models.CharField(max_length=20)
	Description = models.TextField(max_length=500)
	Link = models.CharField(max_length=100)

	def __str__(self):
		return self.Text

	def get_absolute_url(self):
		return reverse('Projects', kwargs={'pk': self.pk})



class about(models.Model):
	Editor = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
	Content = models.TextField(max_length=5000)
