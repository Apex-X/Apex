import click
from telegraph.cmd import generate, header


# main command group
@click.group()
@click.version_option('0.0.1')
def main():
    header()
    pass


main.add_command(
    generate,
)
