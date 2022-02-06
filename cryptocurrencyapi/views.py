import requests
from django.shortcuts import render
from django.conf import settings


def index(request):
    api = requests.get(
        'https://api.coingecko.com/api/v3/coins/markets?vs_currency=brl&order=market_cap_desc&per_page=100&page=1&sparkline=false').json()
    return render(request, 'index.html', {'api': api})
