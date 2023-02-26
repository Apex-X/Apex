from telegraph.build import get_template, ask, generate_project
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
    '--local_path_template',
    type=str,
    default="",
    multiple=False,
    help='path of local template'
)
def generate(git_token: str, vcs_type: str, template_id: int, local_path_template: str):
    """
    Generate project from template in VCS or local path template\n

    [For generating project from VCS]:\n
    $ telegraph generate --git_token "YOUR-TOKEN" --vcs_type "github" --template_id 12456 \n

    [For generating project from local path template]:\n
    $ telegraph generate --local_path_template "YOUR-TEMPLATE-PATH" \n
    """

    if local_path_template:
        selected_tags, selected_vars, destination_path, project_name = ask(local_path_template)
        generate_project(local_path_template, destination_path, project_name, selected_tags, selected_vars)
    else:
        tmp = get_template(git_token, vcs_type, template_id)
        selected_tags, selected_vars, destination_path, project_name = ask(tmp.name)
        generate_project(tmp.name, destination_path, project_name, selected_tags, selected_vars)
        tmp.cleanup()


