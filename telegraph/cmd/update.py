from telegraph.build import get_template, ask, generate_project
import click


@click.command("update")
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
def update(git_token: str, vcs_type: str, template_id: int, local_template_path: str):
    if local_template_path:
        selected_tags, selected_vars, local_project_path, _ = ask(local_template_path, False, True)
        update_project(local_template_path,
                       local_project_path,
                       selected_tags,
                       selected_vars,
                       )
    # else:
    #     tmp = get_template(git_token, vcs_type, template_id)
    #     selected_tags, selected_vars, destination_path, project_name = ask(tmp.name)
    #     generate_project(tmp.name, destination_path, project_name, selected_tags, selected_vars)
    #     tmp.cleanup()