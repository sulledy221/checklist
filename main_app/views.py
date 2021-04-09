from django.shortcuts import redirect, render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Checklist, Vacation
from .forms import RelaxForm


def home(request):
    return redirect('/checklists/')


def about(request):
    return render(request, 'about.html')


def base(request):
    return render(request, 'base.html')


def checklists_index(request):
    checklists = Checklist.objects.all()
    return render(request, 'checklists/index.html', {'checklists': checklists })


def checklists_detail(request, checklist_id):
    checklist = Checklist.objects.get(id=checklist_id)
    vacations_checklist_doesnt_have = Vacation.objects.exclude(id__in = checklist.vacations.all().values_list('id'))
    relax_form = RelaxForm()
    return render(request, 'checklists/detail.html', { 'checklist': checklist, 'relax_form': relax_form, 'vacations': vacations_checklist_doesnt_have })


class ChecklistCreate(CreateView):
    model = Checklist
    fields = ['name', 'task', 'description', 'timeslot']
    success_url = '/checklists/'


class ChecklistUpdate(UpdateView):
    model = Checklist
    fields = ['task', 'description', 'timeslot']


class ChecklistDelete(DeleteView):
    model = Checklist
    success_url = '/checklists/'

def add_rest(request, checklist_id):
    form = RelaxForm(request.POST)
    if form.is_valid():
        new_rest = form.save(commit=False)
        new_rest.checklist_id = checklist_id
        new_rest.save()
    return redirect('detail', checklist_id=checklist_id)

def assoc_vacation(request, checklist_id, vacation_id):
    Checklist.objects.get(id=checklist_id).vacations.add(vacation_id)
    return redirect('detail', checklist_id=checklist_id)
