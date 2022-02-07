from django.shortcuts import render, redirect
from openpyxl import Workbook, load_workbook
from .models import ImportsFile
from .forms import ImportsFileForms
from django.contrib import messages
from django.contrib.auth.decorators import login_required

"""
Aqui vai ser renderização da pagina e leitura dos arquivos importados

"""


@login_required
def template(request):
    if request.method == 'POST':
        form = ImportsFileForms(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            messages.success(request, 'Arquivo Importado com sucesso!')
            return redirect('imports:import-and-read')
        else:
            form = ImportsFileForms()
            messages.error(request, 'Ops, Algo deu errado!')
            
    else:
        form = ImportsFileForms(request.POST, request.FILES)
        return render(request, 'import.html', {'form': form})


def read_archive(request):
    filepath = 'imports/%m/%Y/'
    wb = load_workbook(filepath)
