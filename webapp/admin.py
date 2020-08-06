from django.contrib import admin
from .models import Company_detailes
# Register your models here.
@admin.register(Company_detailes)
class adnimForm(admin.ModelAdmin):
     list_display = ('Company','Division','Sector','Phone','Fax')