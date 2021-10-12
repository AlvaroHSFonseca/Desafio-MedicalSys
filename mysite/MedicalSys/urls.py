from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('pacientes/', views.pacientes, name="pacientes"),
    path('novoPaciente/', views.novoPaciente, name="novoPaciente"),
    path('pacientes/<int:id>', views.delete_paciente, name="delete_paciente"),
    path('update_paciente/<int:pk>', views.update_paciente, name="update_paciente"),
    path('novoMedico/', views.novoMedico, name="novoMedico"),
    path('medicos/', views.medicos, name="medicos"),
    path('modicos/<int:id>', views.delete_medico, name="delete_medico"),
    path('update_medico/<int:pk>', views.update_medico, name="update_medico"),
]