from typing import List, AnyStr
from .apex_syntax import get_vars, get_tag
import os


def generate_project(tmp_dir: str, dst_dir: str, project_name: str, selected_tags: set, selected_vars: dict) -> None:
    """
    Generate project from template

    :param tmp_dir: template directory
    :param dst_dir: destination directory
    :param project_name: project name
    :param selected_tags: selected tags from template by user
    :param selected_vars: selected variables from template by user
    """

    if os.path.exists(os.path.join(dst_dir, project_name)):
        raise FileExistsError(f"{dst_dir} already exists")
    os.mkdir(os.path.join(dst_dir, project_name))
    __generate_files(tmp_dir, os.path.join(dst_dir, project_name), selected_tags, selected_vars)


def __generate_files(tmp_dir: str, dst_dir: str, selected_tags: set, selected_vars: dict) -> None:
    """
    Generate files from template and write them to destination directory recursively

    :param tmp_dir: template directory
    :param dst_dir: destination directory
    :param selected_tags: selected tags from template by user
    :param selected_vars: selected variables from template by user
    """
    for filename in os.scandir(tmp_dir):
        if filename.is_file():
            content: List[AnyStr] = []
            with open(filename.path, "r") as f:
                ignore_flag = False
                for line in f.readlines():
                    if "@apex:end" in line:
                        ignore_flag = False
                        continue
                    if ignore_flag:
                        continue

                    tag = get_tag(line)
                    if tag != "":
                        if tag not in selected_tags:
                            ignore_flag = True
                        continue

                    var_list = get_vars(line, "")
                    if len(var_list):
                        for var_key in var_list:
                            if var_key in selected_vars:
                                line = line.replace(f"@apex:{var_key}:var", selected_vars[var_key])
                            else:
                                raise ValueError(f"Variable {var_key} not found in selected variables")

                    content.append(line)
            __write_file(os.path.join(dst_dir, filename.name), content)

        elif filename.is_dir():
            dir_name = filename.name

            tag = get_tag(dir_name)
            if tag != "":
                if tag not in selected_tags:
                    continue
                dir_name = dir_name.replace(f"@apex:{tag}:tag", "")

            var_list = get_vars(dir_name, "")
            if len(var_list):
                for var_key in var_list:
                    if var_key in selected_vars:
                        dir_name = dir_name.replace(f"@apex:{var_key}:var", selected_vars[var_key])
                    else:
                        raise ValueError(f"Variable {var_key} not found in selected variables")

            os.mkdir(os.path.join(dst_dir, dir_name))
            __generate_files(filename.path, os.path.join(dst_dir, dir_name), selected_tags, selected_vars)


def __write_file(path: str, content: List[AnyStr]) -> None:
    """
    Write content to file
    
    :param path: file path
    :param content: file content
    """
    with open(path, "w") as f:
        f.writelines(content)
