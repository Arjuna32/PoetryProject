import click
import ctypes
import requests
import json


api_key = "949680e5e6bc4f5ea9c1b99492f824ef"

@click.command()
def cli():
    """
    Get the latest news headline
    """
    url = "https://newsapi.org/v2/top-headlines"
    params = {
        "apiKey": api_key,
        "country": "us",  # change this to the country of your choice
    }

    # Send a GET request to the API endpoint
    response = requests.get(url, params=params)

    # Parse the JSON response and extract the latest headline
    data = json.loads(response.text)
    articles = data["articles"]
    titles = [article["title"] for article in articles]

    # Return the latest headline
    for title in titles:
        print(title)


if __name__ == '__main__':
    cli() # pylint: disable=no-value-for-parameter # pragma: no cover
