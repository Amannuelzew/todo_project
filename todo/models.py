from django.db import models

# Create your models here.

class Todo(models.Model):
    title=models.CharField(max_length=50)
    is_completed=models.BooleanField(default=False)
    date=models.DateField(auto_now_add=True)
