""" Modern Python - Get random fact from wikipedia """

import locale
import textwrap
from typing import Tuple

import click
import requests
from requests.exceptions import HTTPError

from . import __version__

API_URL = "https://{language}.wikipedia.org/api/rest_v1/page/random/summary"


@click.command()
@click.option(
    "--language",
    "-l",
    default="local",
    help="Language edition of Wikipedia",
    metavar="LANG",
    show_default=True,
)
@click.version_option(version=__version__)
def main(language: str = "en"):
    """The hypermodern Python project."""

    if language.lower() == "local":
        lang: Tuple[str | None, str | None] = locale.getlocale(locale.LC_CTYPE)
        if lang[0] is not None:
            language = lang[0][:2]

    url = API_URL.format(language=language)
    with requests.get(url, timeout=5) as response:
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
