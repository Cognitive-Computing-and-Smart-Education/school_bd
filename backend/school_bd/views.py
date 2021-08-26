from django.shortcuts import redirect
from login.models import *


def index(request):
    return redirect('/login/')
