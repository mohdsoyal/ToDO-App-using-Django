from django.db import models

# Create your models here.
class ToDOclass(models.Model):
    subject=models.CharField(max_length=100)
    description=models.TextField(max_length=200)
    task_Assign_by=models.CharField(max_length=100)
    task_complete_to=models.CharField(max_length=100)
    Complete_By=models.DateField()
    
