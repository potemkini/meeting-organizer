from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.views.decorators.csrf import csrf_exempt
# import requests
from api.models import *
from functools import wraps
import time

def view_404(request, exception=None):
    return redirect('/') 

def view_500(request, exception=None):
    return redirect('/') 

def redirect_homepage_to_api(request):
    return redirect('/api-v1/docs')