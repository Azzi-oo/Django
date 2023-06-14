from django.http import HttpResponse


def index(request):
    return HttpResponse('ПРИВЕТ МИР')


def test(request):
    return HttpResponse('TEEEESSSTSSSSS')
