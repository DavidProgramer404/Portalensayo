from django.contrib import admin
from main.models import Nota, UserProfile ,Categoria, Equipo
# Register your models here.
class NotaAdmin(admin.ModelAdmin):
  pass

class UserProfileAdmin(admin.ModelAdmin):
  pass

# Categoria

class CategoriaAdmin(admin.ModelAdmin):
      pass

# Equipo
class EquipoAdmin(admin.ModelAdmin):
      pass

admin.site.register(Categoria, CategoriaAdmin)

admin.site.register(Equipo, EquipoAdmin)

admin.site.register(Nota, NotaAdmin)

admin.site.register(UserProfile, UserProfileAdmin)