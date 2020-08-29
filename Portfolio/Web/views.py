from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView, UpdateView, DeleteView, RedirectView
from .forms import language_f, technology_f, projects_f, contact_f
from .models import skills, languages, technologies, projects, about


from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required

from django.core.mail import send_mail


def home_view(request):

	front_end = skills.objects.filter(Field = 'Front-end')
	back_end = skills.objects.filter(Field = 'Back-end')

	language_ = languages.objects.all()
	tech = technologies.objects.all()
	return render(request, 'Web/home.html', {'frontend':front_end,
											 'backend': back_end,
											 'languages':language_,
											 'tech': tech})

def projects_view(request):
	projects_ = projects.objects.all()
	return render(request, 'Web/projects.html', {'projects':projects_})


def about_view(request):
	about_ = about.objects.all()
	return render(request, 'Web/about.html', {'about':about_})


def contact_view(request):
	captcha = contact_f()
	if request.method == 'POST':

		subject = request.POST.get('Name', '')
		from_email = request.POST.get('Email', '')
		message = request.POST.get('Message', '')

		


		send_mail(f"Message from {subject}",
			message,
			from_email,
			['oltlatifi2003@gmail.com'],
			)

		return render(request, 'Web/contact.html', {'name':subject, 'captcha':captcha})
	else:
		return render(request, 'Web/contact.html', {'captcha':captcha})

class skills_v(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
	model = skills
	template_name = 'Web/change_skills.html'
	fields = ['Text']
	success_url = '/'

	def test_func(self):
		skills = self.get_object()
		if self.request.user == skills.Editor:
			return True
		return False










# languages model
class crud(LoginRequiredMixin, UserPassesTestMixin, DetailView):
	model = languages

	def test_func(self):
		skills = self.get_object()
		if self.request.user == skills.Editor:
			return True
		return False


class crudL_update(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
	model = languages
	template_name = 'Web/change_skills.html'
	fields = ['Text']
	success_url = '/'

	def test_func(self):
		skills = self.get_object()
		if self.request.user == skills.Editor:
			return True
		return False



class crudL_delete(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
	model = languages
	template_name = 'Web/delete.html'
	success_url = '/'


	def test_func(self):
		skills = self.get_object()
		if self.request.user == skills.Editor:
			return True
		return False

@login_required
def add_language(request):
	if request.method == "POST":
		form = language_f(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			return redirect("Home")
	else:
		form = language_f()
	return render(request, 'Web/addsomething.html', {'form': form})


# technologies










class crud_tech(LoginRequiredMixin, UserPassesTestMixin, DetailView):
	model = technologies
	template_name = 'Web/technologies_detail.html'

	def test_func(self):
		skills = self.get_object()
		if self.request.user == skills.Editor:
			return True
		return False


class crudT_update(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
	model = technologies
	template_name = 'Web/change_skills.html'
	fields = ['Language','Text']
	success_url = '/'

	def test_func(self):
		skills = self.get_object()
		if self.request.user == skills.Editor:
			return True
		return False



class crudT_delete(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
	model = technologies
	template_name = 'Web/delete.html'
	success_url = '/'

	def test_func(self):
		skills = self.get_object()
		if self.request.user == skills.Editor:
			return True
		return False

@login_required
def add_technology(request):
	if request.method == "POST":
		form = technology_f(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			return redirect("Home")
	else:
		form = technology_f()
	return render(request, 'Web/addsomething.html', {'form': form})









class projects_detail(DetailView):
	model = projects



class projects_update(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
	model = projects
	template_name = 'Web/projects_update.html'
	fields = ['Text','Link','Description']
	success_url = '/projects'

	def test_func(self):
		thing = self.get_object()
		if self.request.user == thing.Editor:
			return True
		return False


class projects_delete(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
	model = projects
	template_name = 'Web/delete.html'
	success_url = '/projects'

	def test_func(self):
		projects = self.get_object()
		if self.request.user == projects.Editor:
			return True
		return False


@login_required
def add_projects(request):
	if request.method == "POST":
		form = projects_f(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			return redirect("Projects")
	else:
		form = projects_f()
	return render(request, 'Web/projects_update.html', {'form': form})


