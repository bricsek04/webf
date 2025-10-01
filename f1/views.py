from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from .models import Team, Driver
from .forms import DriverForm, TeamForm

# Create your views here.

@login_required
def home(request):
    teams = Team.objects.all().prefetch_related('driver_set')
    unassigned_drivers = Driver.objects.filter(team__isnull=True)
    return render(request, 'home.html', {
        'teams': teams,
        'unassigned_drivers': unassigned_drivers,
    })

@login_required
def driver_list(request):
    if not request.user.is_superuser:
        raise PermissionDenied
    drivers = Driver.objects.select_related('team').all()
    return render(request, 'driver_list.html', {'drivers': drivers})

@login_required
def driver_add(request):
    if not request.user.is_superuser:
        raise PermissionDenied
    if request.method == 'POST':
        form = DriverForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('driver-list')
    else:
        form = DriverForm()
    return render(request, 'driver_form.html', {'form': form, 'title': 'Új sofőr hozzáadása'})

@login_required
def driver_edit(request, pk):
    if not request.user.is_superuser:
        raise PermissionDenied
    driver = get_object_or_404(Driver, pk=pk)
    if request.method == 'POST':
        form = DriverForm(request.POST, instance=driver)
        if form.is_valid():
            form.save()
            return redirect('driver-list')
    else:
        form = DriverForm(instance=driver)
    return render(request, 'driver_form.html', {'form': form, 'title': 'Sofőr szerkesztése'})

@login_required
def driver_delete(request, pk):
    if not request.user.is_superuser:
        raise PermissionDenied
    driver = get_object_or_404(Driver, pk=pk)
    driver.delete()
    return redirect('driver-list')

@login_required
def team_list(request):
    if not request.user.is_superuser:
        raise PermissionDenied
    teams = Team.objects.all()
    return render(request, 'team_list.html', {'teams': teams})

@login_required
def team_add(request):
    if not request.user.is_superuser:
        raise PermissionDenied
    if request.method == 'POST':
        form = TeamForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('team-list')
    else:
        form = TeamForm()
    return render(request, 'team_form.html', {'form': form, 'title': 'Új csapat hozzáadása'})

@login_required
def team_edit(request, pk):
    if not request.user.is_superuser:
        raise PermissionDenied
    team = get_object_or_404(Team, pk=pk)
    if request.method == 'POST':
        form = TeamForm(request.POST, instance=team)
        if form.is_valid():
            form.save()
            return redirect('team-list')
    else:
        form = TeamForm(instance=team)
    return render(request, 'team_form.html', {'form': form, 'title': 'Csapat szerkesztése'})

@login_required
def team_delete(request, pk):
    if not request.user.is_superuser:
        raise PermissionDenied
    team = get_object_or_404(Team, pk=pk)
    team.delete()
    return redirect('team-list')