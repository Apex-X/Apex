from typing import Tuple, Set, Dict
import typer


def ask_questions(
        tags: Set[str],
        vars_to_tag: Dict[str, str],
) -> Tuple[Set[str], Dict[str, str], str, str]:
    """
    Ask user for project name, path, tags and variables

    :param tags: set of all tags
    :param vars_to_tag: map of variables to tag
    :return: selected_tags, selected_variables_with_value, project_path, project_name
    """
    project_name = typer.prompt(f"🎯 Enter the project name:", default="")

    path = typer.prompt(f"🕹️ Enter the project path:", default="")

    selected_tags = set({})
    for tag in tags:
        flag = typer.confirm(f"🚀 Do you want to use \"{tag}\"?", default=True)
        if flag:
            selected_tags.add(tag)

    selected_variables_with_value = {}
    for var, tag in vars_to_tag.items():
        if tag != "" and tag not in selected_tags:
            continue
        value = typer.prompt(f"🛎️ Enter the value of \"{var}\" variable:", default="")
        if value:
            selected_variables_with_value[var] = value

    return selected_tags, selected_variables_with_value, path, project_name
