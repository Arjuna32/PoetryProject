import requests
import click
import ctypes
#pip install requests
#do that after poetry shell

@click.command(no_args_is_help=True, help = "if you want to check the weather for a given city use the command --city or -c followed by city name ")
@click.option("--city", "-c", help = "city name")
def cli(city):
    api_key = "3a4a4990ecc0d7999cb063b243b1b089"
    # Build the API URL with the city and API key
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&APPID={api_key}"
    #http://api.openweathermap.org/data/2.5/weather?q={city}&APPID={api_key}
    
    # Make the API call and get the response
    response = requests.get(url)
    
    # Parse the JSON response into a Python dictionary
    data = response.json()
    
    
    # Get the relevant weather information from the dictionary
    description = data['weather'][0]['description']
    temp = data['main']['temp']
    feels_like = data['main']['feels_like']
    humidity = data['main']['humidity']
    
    # Convert temperature from Kelvin to Celsius
    temp_celsius = round(temp - 273.15, 2)
    feels_like_celsius = round(feels_like - 273.15, 2)
    
    # Print the weather information
    print(f"Current weather in {city}: {description}")
    print(f"Temperature: {temp_celsius}°C")
    print(f"Feels like: {feels_like_celsius}°C")
    print(f"Humidity: {humidity}%")

