from django.shortcuts import render
from django.http import HttpResponse


def car(request):
    return render(request, 'car_templates/car.html')


def create(request, id):
    output = '<h2>Cars</h2><h3>Car ID: {0}</h3>'.format(id)
    return HttpResponse(output)


def info(request, id):
    output = '<h2>Car info</h2><h3>Car ID: {0}</h3>'.format(id)
    return HttpResponse(output)


def id_car(request, id):
    output = '<h2>Car ID: {0}</h2>'.format(id)
    return HttpResponse(output)