from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
# from django.urls import reverse
from sys_endereco.models import Endereco
from sys_endereco.forms import cadForm
from django.core.exceptions import ValidationError
# Create your views here.
def index(request):#Homepage
    addresses = Endereco.objects.values()
    listadd = list(addresses)
    values = []
    for data in listadd:
        values.append(list(data.values()))
    context = {
        'addresses': values,
    }
    return render(request, 'index.html', context=context)

def cadastro(request):#Cadpage
    form = cadForm();
    if request.method == 'POST':
        form = cadForm(request.POST);
        if form.is_valid():
            data_cep = form.cleaned_data['cep']
            data_logr = form.cleaned_data['logradouro']
            data_bai = form.cleaned_data['bairro']
            data_num = form.cleaned_data['numero']
            data_cid = form.cleaned_data['cidade']
            data_uf = form.cleaned_data['uf']
            data_compl = form.cleaned_data['complemento']
            data_desc = form.cleaned_data['descricao']
            temp = Endereco.objects.filter(cep=data_cep)

            new_add = Endereco(cep=data_cep,logradouro=data_logr,bairro=data_bai,
            numero=data_num,cidade=data_cid,uf=data_uf,complemento=data_compl,
            descricao=data_desc)
            new_add.save()
            return redirect('index')
    return render(request, 'cad.html', {'form': form})
