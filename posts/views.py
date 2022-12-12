import datetime
from django.shortcuts import HttpResponse


def main(request):
    return HttpResponse('Hello! its my first view!')


def data(request):
    return HttpResponse(datetime.datetime.now())


def good_by(request):
    return HttpResponse('Goodby user!!!')
