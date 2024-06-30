from apex.build import get_blueprint, ask_questions, Apex
import click


@click.command("generate")
@click.option(
    '--git_token',
    type=str,
    default="",
    multiple=False,
    help='git token to get template'
)
@click.option(
    '--vcs_type',
    type=str,
    default="",
    multiple=False,
    help='version control system'
)
@click.option(
    '--template_id',
    type=int,
    default=0,
    multiple=False,
    help='git template code'
)
@click.option(
    '--local_template_path',
    type=str,
    default="",
    multiple=False,
    help='path of local template'
)
def generate(git_token: str, vcs_type: str, template_id: int, local_template_path: str):
    """
    Generate project from template in VCS or local path template\n

    [For generating project from VCS]:\n
    $ apex generate --git_token "YOUR-TOKEN" --vcs_type "github" --template_id 12456 \n

    [For generating project from local path template]:\n
    $ apex generate --local_template_path "YOUR-TEMPLATE-PATH" \n
    """

    apex = Apex()
    if local_template_path:
        tags, vars_to_tag = apex.parse_syntax(local_template_path)
        selected_tags, selected_vars, destination_path, project_name = ask_questions(tags, vars_to_tag)
        apex.generate_project(local_template_path, destination_path, project_name, selected_tags, selected_vars)
    else:
        tmp = get_blueprint(git_token, vcs_type, template_id)
        tags, vars_to_tag = apex.parse_syntax(tmp.name)
        selected_tags, selected_vars, destination_path, project_name = ask_questions(tags, vars_to_tag)
        apex.generate_project(tmp.name, destination_path, project_name, selected_tags, selected_vars)
        tmp.cleanup()
