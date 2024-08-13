from django.db import models

# Create your models here.
class info(models.Model):
  name = models.textField(max_length=100)
  surname = models.textField(max_length=100)
  student_number = models.CharField()
  
  def __str__:
    return info.name
