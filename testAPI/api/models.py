from django.db import models

# Create your models here.
class Worker(models.Model):
  admin_id = models.IntegerField()
  call_date = models.DateField()
  call_time = models.TimeField()
  result = models.BooleanField()

  #models.CharField(max_length=200)    
  # def __str__(self):
  #   return self.worker_name