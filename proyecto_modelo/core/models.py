from django.db import models

# Create your models here.
class Person(models.Model):
    first_name = models.CharField(max_length=30, help_text="first name")
    last_name = models.CharField(max_length=50, help_text="last name")
    age = models.IntegerField(default=18, help_text="age")
    country = models.CharField(max_length=30, help_text="country")
    email = models.EmailField(null=True, blank=True, help_text="email")
    
    class Meta:
        db_table = "persona"
        verbose_name = "Persona"
        verbose_name_plural = "Personas"
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"