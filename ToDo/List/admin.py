from django.contrib import admin
from .models import ToDOclass

# Register your models here.
class ToDOadmin(admin.ModelAdmin):
    list_display=('subject','description','task_Assign_by','task_complete_to','Complete_By')
admin.site.register(ToDOclass,ToDOadmin)


