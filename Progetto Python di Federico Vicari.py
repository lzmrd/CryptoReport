# -*- coding: utf-8 -*-
"""
Created on Wed Mar 31 12:33:40 2021

@author: Federico
"""

import requests
from pprint import pprint
import time
from datetime import datetime
import json
import datetime as dt


class Report:
    
    def __init__(self, params):
        
        self.url  = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
        self.params = params
        self.headers = {
        'Accepts' : 'application/json',
        'X-CMC_PRO_API_KEY' : '599a20cc-0d89-43f8-ac7e-9aad1c775df2',
        }
        
        self.prices = []      
        

    def fetchCurrenciesData(self):
        
        r = requests.get(url=self.url, headers=self.headers, params=self.params).json()

        return r['data']


while(1):  
    data = []

    volume = Report({
    'start' : '1', 
    'limit' : '1',
    'convert' : 'USD',
    'sort' : 'volume_24h',
    })    

    currencies = volume.fetchCurrenciesData()   

    for currency in currencies:
       p1 = ('La cryptovaluta che ha registato i più alti volumi nelle ultime 24 ore è: ', currency['symbol'])

    print(p1)
    
    data.append(p1)


    best = Report({
    'start' : '1', 
    'limit' : '10',
    'convert' : 'USD',
    'sort' : 'percent_change_24h',
    'sort_dir' : 'desc',
    })

    currencies = best.fetchCurrenciesData()
    
    p2 = ("Le 10 cryptovalute che hanno avuto l'incremento di prezzo maggiore nelle ultime 24 ore sono:")
    print(p2)
    
    data.append(p2)

    for currency in currencies:
       p3 = currency['symbol'] + ' = ' + currency['name']
    
       pprint(p3)
    
       data.append(p3)

    worst = Report({
    'start' : '1', 
    'limit' : '10',
    'convert' : 'USD',
    'sort' : 'percent_change_24h',
    'sort_dir' : 'asc',
    })

    currencies = worst.fetchCurrenciesData()
    
    p4= ('Le 10 cryptovalute che hanno avuto il decremento di prezzo maggiore nelle ultime 24 ore sono:')
    print(p4)
    
    data.append(p4)


    for currency in currencies:
       p5 = currency['symbol'] + ' = ' + currency['name']
       pprint(p5)
       
       data.append(p5)


    need = Report({
    'start' : '1', 
    'limit' : '20',
    'convert' : 'USD',
    'sort' : 'market_cap',
    })
    
    currencies = need.fetchCurrenciesData()

    for currency in currencies:
        unit = currency['quote']['USD']['price']
    
        need.prices.append((unit))
    

    total = sum(need.prices)
    
    p6= ('Acquistare una unità delle prime 20 cryptovalute ti costerà: ',total,'$')
    print(p6)
    
    data.append(p6)

    amount = Report({
    'start' : '1', 
    'limit' : '200',
    'convert' : 'USD',
    })

    currencies = amount.fetchCurrenciesData()

    for currency in currencies:
        if currency['quote']['USD']['volume_24h'] > 76000000:
        
            amount.prices.append(currency['quote']['USD']['price'])
        
        price = sum(amount.prices)
        
    p7 = ('Per acquistare una unità di tutte le criptovalute il cui volume delle ultime 24 ore è stato superiore a 76.000.000$, dovrai spendere: ', price, '$')
    print(p7)
    
    data.append(p7)

    yPrices=[]
    prices = []

    currencies = need.fetchCurrenciesData()


    for currency in currencies:
        unit = currency['quote']['USD']['price']
        prices.append((unit))
    
        yPrice = (currency['quote']['USD']['price']*100) / (100+(currency['quote']['USD']['percent_change_24h']))
        yPrices.append(yPrice)


    total = sum(prices)
    tot = sum(yPrices)

    perc= ((total-tot)/tot)*100
    
    

    p8 = ('Per acquistare una unità delle prime 20 cryptovalute per capitalizzazione, 24 ore fa avresti speso: ',tot, '$, ed ora avresti: ', total, '$ con un rendimento del', perc, '%')
    print(p8)
    
    data.append(p8)
    
    c_date= dt.date.today()
    c_date= str(c_date)

    with open('CryptoReport_' + c_date + '.json', "w") as f:
        json.dump(data, f)
        
    minutes = 60
    seconds = minutes * 60
    day= seconds * 24
    time.sleep(day)     
