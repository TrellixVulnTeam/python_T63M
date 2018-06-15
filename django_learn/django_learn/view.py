# -*- utf-8 -*-
from django.http import HttpResponse


def hello(request):
    result = 'hello world'
    return HttpResponse(result)
