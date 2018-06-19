# -*- utf-8 -*-
from django.http import HttpResponse
import os
import subprocess
import pymysql

def hello(request):
    os.system("")
    return HttpResponse("hello")
