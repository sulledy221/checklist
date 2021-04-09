from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('checklists/', views.checklists_index, name='index'),
    path('checklists/<int:checklist_id>/', views.checklists_detail, name='detail'),
    path('checklists/create/', views.ChecklistCreate.as_view(), name='checklists_create'),
    path('checklists/<int:pk>/update/', views.ChecklistUpdate.as_view(), name='checklists_update'),
    path('checklists/<int:pk>/delete/', views.ChecklistDelete.as_view(), name='checklists_delete'),
    path('checklists/<int:checklist_id>/add_rest/', views.add_rest, name='add_rest'),
    path('checklists/<int:checklist_id>/assoc_vacation/<int:vacation_id>/', views.assoc_vacation, name='assoc_vacation'),
]