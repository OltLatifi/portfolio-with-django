from django.contrib import admin
from .models import skills, languages, technologies, projects, about


admin.site.register(skills)
admin.site.register(languages)
admin.site.register(technologies)
admin.site.register(projects)
admin.site.register(about)