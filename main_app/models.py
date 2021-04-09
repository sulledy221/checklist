from django.db import models 
from django.urls import reverse


RELAX = (
    ('M', 'Morning'),
    ('A', 'Afternoon'),
    ('N', 'Night')
)

class Vacation(models.Model):
  name = models.CharField(max_length=50)

class Checklist(models.Model):
  name = models.CharField(max_length=100)
  task = models.CharField(max_length=100)
  description = models.TextField(max_length=250)
  timeslot = models.IntegerField()
  vacations = models.ManyToManyField(Vacation)

  def __str__(self):
    return self.name
    
  # Add this method
  def get_absolute_url(self):
    return reverse('detail', kwargs={'checklist_id': self.id})

class Relax(models.Model):
  date = models.DateField('relax date')
  plannedtime = models.CharField(
    max_length=12,
    choices=RELAX,
    default=RELAX[0][0]
  )

  checklist = models.ForeignKey(Checklist, on_delete=models.CASCADE)

  def __str__(self):
    return f"{self.get_plannedtime_display()} on {self.date}"

  class Meta:
    ordering = ['-date']