from django.http import HttpResponse
from django.shortcuts import render

def login(request):
    return render(request, 'login.html')

def home(request):
    return render(request, 'index.html')

def articles(request, year):
    return HttpResponse ('O ano enviado foi ' +str(year))

def fname (request, nome):
    result = lerdobanco(nome)
    print(result)
    return HttpResponse('A pessoa foi encontranda ela tem ' +str(result['idade']) + ' anos')


def lerdobanco(nome):
    lista_nomes = [
        {'nome': 'Ana', 'idade': '20'},
        {'nome': 'Jorge', 'idade': '25'},
        {'nome': 'Renato', 'idade': '18'}
    ]

    for pessoa in lista_nomes:
        if pessoa['nome'] == nome:
            return pessoa
    else:
        return {'nome': 'Não encontrado', 'idade': 0 }