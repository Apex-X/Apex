from apexx.build import ask_questions, Apex
from typing_extensions import Annotated
import typer

app = typer.Typer()


@app.command()
def generate(
    blueprint_path: Annotated[str, typer.Argument(help="🪙 path of local project template")]
):
    """
    Generate project from template in local path template\n

    $ apexx "YOUR-BLUEPRINT-PATH" \n
    """

    apex = Apex()
    if blueprint_path != "":
        tags, vars_to_tag = apex.parse_syntax(blueprint_path)
        selected_tags, selected_vars, destination_path, project_name = ask_questions(tags, vars_to_tag)
        apex.generate_project(blueprint_path, destination_path, project_name, selected_tags, selected_vars)
    else:
        typer.echo("Please provide blueprint path")
        raise typer.Exit(code=1)
