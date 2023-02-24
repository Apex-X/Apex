import click
from telegraph.cmd import generate_group


# main command group
@click.group()
@click.version_option('0.0.1')
def main():
    pass


main.add_command(
    generate_group,
)
