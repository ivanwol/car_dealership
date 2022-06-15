from django.shortcuts import render
from django.http import HttpResponse


def name(request, id):
    output = '<h2>Dealer name</h2><h3>Dealer ID: {0}</h3>'.format(id)
    return HttpResponse(output)


def id_dealer(request, id):
    output = '<h2>Dealer</h2><h3>Dealer ID: {0}</h3>'.format(id)
    return output


def name_dealer(request):
    id = request.GET.get('id', '')
    name = request.GET.get('name', '')
    output = '<h2>Dealer name: {0}, dealer ID: {1}</h2>'.format(name, id)
    return HttpResponse(output)