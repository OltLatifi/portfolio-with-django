from django.contrib import admin
from django.urls import path
from Web.views import home_view, projects_view, about_view, contact_view
from django.contrib.auth import views as user_views

from Web import views as Views
from Web.models import skills, languages, technologies, projects, about 


# for static images
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
	path('admin/', admin.site.urls),
	path('', home_view, name = 'Home'),
	path('projects/', projects_view, name = 'Projects'),
	path('about/', about_view, name = 'About'),
	path('contact/', contact_view, name = 'Contact'),

	path('skills/<int:pk>/update', Views.skills_v.as_view(model = skills), name ='Skills'),
	path('crud_lang/', Views.add_language, name = 'Crud'),
	path('crud_lang/<int:pk>', Views.crud.as_view(model = languages), name = 'Crud-lang'),
	path('crud_lang/<int:pk>/update', Views.crudL_update.as_view(model = languages), name = 'Crud-lang-update'),
	path('crud_lang/<int:pk>/delete', Views.crudL_delete.as_view(model = languages), name = 'Crud-lang-delete'),
	
	path('superuserMode-view/', user_views.LoginView.as_view(template_name='Web/login.html'), name='Login'),
	path('usermode-view/', user_views.LogoutView.as_view(template_name='Web/logout.html'), name='Logout'),

	path('crud_tech/', Views.add_technology, name = 'CrudT'),
	path('crud_tech/<int:pk>', Views.crud_tech.as_view(model = technologies), name = 'Crud-tech'),
	path('crud_tech/<int:pk>/update', Views.crudT_update.as_view(model = technologies), name = 'Crud-tech-update'),
	path('crud_tech/<int:pk>/delete', Views.crudT_delete.as_view(model = technologies), name = 'Crud-tech-delete'),


	path('add_project', Views.add_projects, name = 'Projects-add'),
	path('projects/<int:pk>', Views.projects_detail.as_view(model = projects), name = 'Projects'),
	path('projects/<int:pk>/update', Views.projects_update.as_view(model = projects), name = 'Projects-update'),
	path('projects/<int:pk>/delete', Views.projects_delete.as_view(model = projects), name = 'Projects-delete'),

	path('about/<int:pk>', Views.about_detail.as_view(model = about), name = 'About-det'),
	path('about/<int:pk>/update', Views.about_update.as_view(model = about), name = 'About-update'),
	path('about/<int:pk>/delete', Views.about_delete.as_view(model = about), name = 'About-delete'),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
