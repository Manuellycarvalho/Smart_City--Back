from django.shortcuts import render
from django.http import HttpResponse

def abre_index(request):
    messagem = "Turma DS2 "
    return HttpResponse(messagem)


def cad_user(request):
    return render(request, 'Cad_User_Api.html')