from typing import List, AnyStr
from .telegraph_lang import get_vars, get_tag
import os

def update_project(
        local_template_path: str,
        local_project_path: str,
        selected_tags: set,
        selected_vars: dict
) -> None:
    """
    Update project from template

    :param local_template_path: template directory
    :param local_project_path: project directory
    :param selected_tags: selected tags from template by user
    :param selected_vars: selected variables from template by user
    """
    if not os.path.exists(local_project_path):
        raise FileNotFoundError(f"{local_project_path} not found")
    __update_files(local_template_path, local_project_path, selected_tags, selected_vars, False)

def __update_files(
        local_template_path: str,
        local_project_path: str,
        selected_tags: set,
        selected_vars: dict,
        insert_file: bool
) -> None:
    

