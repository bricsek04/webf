from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView
from .models import Team, Driver
from .forms import DriverForm

# Create your views here.

@login_required(login_url='login')
def home(request):
    teams = Team.objects.all().prefetch_related('driver_set')
    unassigned_drivers = Driver.objects.filter(team__isnull=True)

    if request.method == 'POST':
        form = DriverForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = DriverForm()

    return render(request, 'home.html', {
        'teams': teams,
        'unassigned_drivers': unassigned_drivers,
        'form': form,
    })

@login_required(login_url='login')
def delete_driver(request, pk):
    driver = get_object_or_404(Driver, pk=pk)
    driver.delete()
    return redirect('home')

@login_required(login_url='login')
def assign_team(request, pk):
    driver = get_object_or_404(Driver, pk=pk)
    if request.method == 'POST':
        team_id = request.POST.get('team')
        if team_id:
            driver.team_id = team_id
            driver.save()
    return redirect('home')