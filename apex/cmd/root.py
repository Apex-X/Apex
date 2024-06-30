import click
from .generate import generate


@click.group()
def cli():
    pass


cli.add_command(generate)
