from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('base/', views.base, name='base'),
    path('checklists/', views.checklists_index, name='index'),
    path('checklists/<int:checklist_id>/', views.checklists_detail, name='detail'),
    path('checklists/create/', views.ChecklistCreate.as_view(), name='checklists_create'),
    path('checklists/<int:pk>/update/', views.ChecklistUpdate.as_view(), name='checklists_update'),
    path('checklists/<int:pk>/delete/', views.ChecklistDelete.as_view(), name='checklists_delete'),
]