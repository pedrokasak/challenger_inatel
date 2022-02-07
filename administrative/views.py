from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
import requests


@staff_member_required
@login_required
def index(request):
    return render(request, 'index.html')


def list_index(request):
    api = requests.get(
        'https://api.coingecko.com/api/v3/coins/markets?vs_currency=brl&order=market_cap_desc&per_page=5&page=1&sparkline=false').json()
    return render(request, 'index.html', {'api': api})
