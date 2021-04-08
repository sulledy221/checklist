from django.shortcuts import redirect, render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Checklist
from django.http import HttpResponse
from .models import Checklist

def home(request):
  return redirect('/checklist/')

# Create your views here.
def about(request):
    return render(request, 'about.html')
    
def base(request):
    return render(request, 'base.html')

def checklists_index(request):
  checklists = Checklist.objects.all()
  return render(request, 'checklists/index.html', { 'checklists': checklists })

def checklists_detail(request, checklist_id):
  checklist = Checklist.objects.get(id=checklist_id)
  return render(request, 'checklists/detail.html', { 'checklist': checklist })


class ChecklistCreate(CreateView):
  model = Checklist
  fields = '__all__'
  success_url = '/checklists/'

class ChecklistUpdate(UpdateView):
  model = Checklist
  fields = ['task', 'description', 'timeslot']

class ChecklistDelete(DeleteView):
  model = Checklist
  success_url = '/checklists/'