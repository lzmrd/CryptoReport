# Crypto Report

This program uses Coinmarketcap API to get all cryptocurrencies data. It analyzes them and can extract some of them according to set values. It gives you information about:
* the cryptocurrency with higher volume in the last 24 hours
* The amount of USD needed to buy 1 token of first 20 cryptocurrencies in market cap
* The percentage of USD gained (or lost) if 24 hours before we bought 1 token of first 20 cryptocurrencies in market cap
* The amount of USD needed to buy 1 token of each cryptocurrency had a volume of trading higher than 76.000.000$ in last 24 hours
* The best, and the worst, 10 cryptocurrencies in last 24 hours

If you want to try it, you should use:
``` pip install requests ```
* python
* install "requests" library through pip
* get your API key here: https://coinmarketcap.com/api/
* insert your api key in line 21 of main.py
* run the program
* enjoy your data

You can even develop this to make a bot which buys and sells if price goes up or down (according to your parameters)
