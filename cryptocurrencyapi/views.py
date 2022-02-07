import requests
from django.shortcuts import render


"""
Consumo de Api ao clickar no botao Mercado Crypto

"""

def list(request):
    api = requests.get(
        'https://api.coingecko.com/api/v3/coins/markets?vs_currency=brl&order=market_cap_desc&per_page=50&page=1&sparkline=false').json()
    return render(request, 'list-crypto.html', {'api': api})
