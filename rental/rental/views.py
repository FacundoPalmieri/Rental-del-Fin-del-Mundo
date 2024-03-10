from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.conf import settings
from django.urls import reverse
import requests
from .forms import *
from django.views.decorators.csrf import csrf_exempt
from django.core.cache import cache
from django.utils import timezone
import json
from django.core.exceptions import ObjectDoesNotExist
from datetime import datetime, timedelta

def homepage(request):
    return render(request, 'index.html')