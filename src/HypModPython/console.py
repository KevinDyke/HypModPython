# src/HypModPython/console.py 
import textwrap

import click
import requests
from requests.exceptions import HTTPError

from . import __version__

API_URL: str = "https://{language}.wikipedia.org/api/rest_v1/page/random/summary"

@click.command()
@click.option(
    "--language",
    "-l",
    default="en",
    help="Language edition of Wikipedia",
    metavar="LANG",
    show_default=True,
)
@click.version_option(version=__version__)
def main(language: str = "en"):
    """ The hypermodern Python project."""
    url = API_URL.format(language=language)
    with requests.get(url) as response:
        try:
            response.raise_for_status()
        
            if response.status_code == 200:
                data = response.json()

                title = data["title"]
                extract = data["extract"]

                click.secho(title, fg="green")
                click.echo(textwrap.fill(extract))
            else:
                click.echo("Something went wrong!")
        except HTTPError as http_err:
            click.echo(f"HTTP error occurred: {http_err}")
