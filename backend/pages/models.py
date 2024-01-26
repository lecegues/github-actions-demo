from django.db import models

# Create your models here.
# where we define database models which Django automatically translates into database tables
class Student(models.Model):
    name=models.CharField(max_length=100)
    des=models.TextField()
    def __str__(self):
        return self.name

