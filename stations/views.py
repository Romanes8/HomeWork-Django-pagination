from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.paginator import Paginator
import csv


def index(request):
    return redirect(reverse('bus_stations'))


def bus_stations(request):
    with open('data-398-2018-08-30.csv', newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        bus_stations = []
        for row in reader:
            bus_stations.append({'Name': row['Name'], 'Street': row['Street'], 'District': row['District']})
        paginator = Paginator(bus_stations, 10)
        page_number = int(request.GET.get('page', 1))
        page = paginator.get_page(page_number)
        context = {
            'page': page,
        }
        return render(request, 'stations/index.html', context)
