from django.http.request import HttpRequest
from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from .models import Medicos, Pacientes
from .form import pacienteForm, medicoForm
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy

# Create your views here.



@login_required
def index(request):
    return render(request, 'MedicalSys/index.html')

@login_required
def pacientes(request):
    dadosPaciente = Pacientes.objects.order_by('-data')[:6]
    context = {'dadosPaciente': dadosPaciente}
    return render( request, 'MedicalSys/pacientes.html', context)

@login_required
def novoPaciente(request):
    form = pacienteForm(request.POST or None)
    

    if form.is_valid():
        form.save()
        return redirect('pacientes')

    return render(request, 'MedicalSys/novoPaciente.html', {'form': form})

@login_required
def update_paciente(request, pk):
    dadosPaciente = Pacientes.objects.get(pk=pk)
    form = pacienteForm(request.POST or None, instance=dadosPaciente)    

    if form.is_valid():
        form.save()
        return redirect('pacientes')

    return render(request, 'MedicalSys/updatePaciente.html', {'form': form})

def delete_paciente(request, id):
    deletePaciente = Pacientes.objects.get(id=id)
    deletePaciente.delete()
    return redirect('pacientes')

@login_required
def medicos(request):
    dadosMedicos = Medicos.objects.order_by('-data')[:6]
    context = {'dadosMedicos': dadosMedicos}
    return render(request, 'MedicalSys/medicos.html', context)

@login_required
def novoMedico(request):
    form = medicoForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('medicos')

    return render(request, 'MedicalSys/novoMedico.html', {'form' : form})

def delete_medico(request, id):
    deleteMedico = Medicos.objects.get(id=id)
    deleteMedico.delete()
    return redirect('medicos')

@login_required
def update_medico(request, pk):
    dadosMedico = Medicos.objects.get(pk=pk)
    form = medicoForm(request.POST or None, instance=dadosMedico)    

    if form.is_valid():
        form.save()
        return redirect('medicos')

    return render(request, 'MedicalSys/updateMedico.html', {'form': form})