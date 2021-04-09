from django.forms import ModelForm
from .models import Relax

class RelaxForm(ModelForm):
  class Meta:
    model = Relax
    fields = ['date', 'plannedtime']