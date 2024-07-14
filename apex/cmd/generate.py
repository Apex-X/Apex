from apex.build import get_blueprint, ask_questions, Apex
import click


@click.command("generate")
@click.option(
    '--blueprint_path',
    type=str,
    default="",
    multiple=False,
    help='path of local project template'
)
def generate(blueprint_path: str):
    """
    Generate project from template in VCS or local path template\n

    [For generating project from local path template]:\n
    $ apex generate --blueprint_path "YOUR-TEMPLATE-PATH" \n
    """

    apex = Apex()
    if blueprint_path:
        tags, vars_to_tag = apex.parse_syntax(blueprint_path)
        selected_tags, selected_vars, destination_path, project_name = ask_questions(tags, vars_to_tag)
        apex.generate_project(blueprint_path, destination_path, project_name, selected_tags, selected_vars)
