from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Transacao
from .form import TransacaoForm


# Create your views here.
def home(request):
    data = {}
    data['transacoes'] = ['t1','t2','t3']
    # now = datetime.datetime.now()
    # html = "<html><body>It is now %s.</body></html>" % now
    return render(request,'home.html')

def listagem(request):
    data = {}
    data['transacoes'] = Transacao.objects.all()
    return render(request,'listagem.html',data)

def novaTransacao(request):

    form = TransacaoForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'form.html',{'form':form})

def update(request, pk):

    data = {}

    transacao = Transacao.objects.get(pk=pk)
    form = TransacaoForm(request.POST or None, instance=transacao)

    if form.is_valid():
        form.save()
        return redirect('lista')

    data['form'] = form
    return render(request,'form.html',data)

def delete(request, pk):
    transacao = Transacao.objects.get(pk=pk)
    transacao.delete()
    return redirect('lista')