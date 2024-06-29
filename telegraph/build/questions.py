from .telegraph_lang import parse_telegraph_annotations
from typing import Tuple, Set, Dict
import typer


def ask(tmp_dir: str, get_project_name: bool, get_project_path: bool) -> Tuple[Set[str], Dict[str, str], str, str]:
    """
    Ask user for project name, path, tags and variables

    :param tmp_dir: template directory
    :param get_project_path: flag to get project path
    :param get_project_name: flag to get project name
    :return: selected_tags, selected_variables, project_path, project_name
    """
    tags, vars = parse_telegraph_annotations(tmp_dir)

    project_name = ""
    if get_project_name:
        project_name = typer.prompt(f"Enter the project name:", default="")

    path = ""
    if get_project_path:
        path = typer.prompt(f"Enter the project path:", default="")

    selected_tags = set({})
    selected_vars = {}
    for tag in tags:
        flag = typer.confirm(f"Do you want to use \"{tag}\"?", default=True)
        if flag:
            selected_tags.add(tag)

    for var_key, var_value in vars.items():
        if var_value != "" and var_value not in selected_tags:
            continue
        value = typer.prompt(f"Enter value for \"{var_key}\" variable:", default="")
        if value:
            selected_vars[var_key] = value

    return selected_tags, selected_vars, path, project_name
