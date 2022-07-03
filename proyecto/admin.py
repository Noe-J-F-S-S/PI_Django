from django.contrib import admin

# Register your models here.
from .models import CursoUser,Cursos,Roles,UserRoles,Users

admin.site.register(CursoUser)
admin.site.register(Cursos)
admin.site.register(Roles)
admin.site.register(UserRoles)
admin.site.register(Users)