from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView
from .models import Team, Driver

# Create your views here.

@login_required(login_url='login')
def home(request):
    return render(request, 'home.html')

class TeamListView(ListView):
    model = Team
    template_name = 'team_list.html'


class DriverListView(ListView):
    model = Driver
    template_name = 'driver_list.html'