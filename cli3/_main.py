from forex_python.converter import CurrencyRates

import click
import ctypes
#pip install forex-python
#do that after poetry shell

@click.command(no_args_is_help=True, help = "to convert from usd to euro call --usd or -u then add the dollar amount")
@click.option("--usd", "-u", help = "USD amount")
def cli(usd):
    usdf = float(usd)
    c = CurrencyRates()
    
    # Get the current exchange rate for USD to Euro
    exchange_rate = c.get_rate('USD', 'EUR')
    
    # Convert the USD amount to Euro
    euro_amount = round(usdf * exchange_rate, 2)
    print(f"{usd} USD is equivalent to {euro_amount} Euros Based on the exchange rate: {exchange_rate}")

def usd_to_euro(usd):
    # Create an instance of the CurrencyRates class
    c = CurrencyRates()
    
    # Get the current exchange rate for USD to Euro
    exchange_rate = c.get_rate('USD', 'EUR')
    
    # Convert the USD amount to Euro
    euro_amount = round(usd * exchange_rate, 2)
    
    # Return the Euro amount
    return euro_amount



