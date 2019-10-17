from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.urls import reverse
import datetime
from django.utils import timezone

from .models import Profile, Competition

# Create your views here.
def index(request):
    compList = Competition.objects.all()
    context = {'compList': compList}
    return render(request, 'comp/index.html', context)