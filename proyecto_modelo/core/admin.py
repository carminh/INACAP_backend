from django.contrib import admin
from .models import Person

class PersonAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "age", "country", "email")
    search_fields = ("first_name", "last_name", "age", "country", "email")
    list_filter = ("age", "country")
    list_per_page = 10
    fieldsets = (
        ("Datos Personales", {"fields": ("first_name", "last_name")}),
        ("Datos Adicionales", {"fields": ("email", "age", "country")}),
    )


# Register your models here.
admin.site.register(Person, PersonAdmin)