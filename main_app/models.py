from django.db import models 
from django.urls import reverse

class Checklist(models.Model):
  name = models.CharField(max_length=100)
  task = models.CharField(max_length=100)
  description = models.TextField(max_length=250)
  timeslot = models.IntegerField()

  def __str__(self):
    return self.name
    
  # Add this method
  def get_absolute_url(self):
    return reverse('detail', kwargs={'checklist_id': self.id})