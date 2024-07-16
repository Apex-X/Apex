import os
import re
from typing import Tuple, Set, Dict, List, AnyStr


class Apex:

    def __init__(self):
        ...

    @staticmethod
    def __get_vars(text: str, scope_tag: str) -> Dict[str, str]:
        """
        Get variables from input text

        :param text: text to parse
        :param scope_tag: tag of variable
        :return: variables
        """
        vars = {}
        var_regex = re.compile(r"@apex:\w+:var")
        if var_regex.findall(text):
            var_list = var_regex.findall(text)
            for var in var_list:
                if var and var not in vars:
                    var = var.split(":")[1]
                    vars[var] = scope_tag
        return vars

    @staticmethod
    def __get_tag(text: str) -> str:
        tag_regex = re.compile(r"@apex:\w+:tag")
        if tag_regex.findall(text):
            tag = tag_regex.findall(text)[0]
            tag = tag.split(":")[1]
            return tag
        return ""

    def parse_syntax(self, blueprint_dir: str) -> Tuple[Set[str], Dict[str, str]]:
        """
        Parse apex annotations from template

        :param blueprint_dir: template directory
        :return: tags, variables
        """
        tags = set({})
        vars_to_tag = {}
        for filename in os.scandir(blueprint_dir):
            if filename.is_file():
                with open(filename.path, "r") as f:
                    scope_tag = ""
                    for line in f.readlines():
                        tag = self.__get_tag(line)
                        if tag != "" and tag not in tags:
                            tags.add(tag)
                            scope_tag = tag

                        var_list = self.__get_vars(line, scope_tag)
                        if len(var_list):
                            vars_to_tag.update(var_list)

                        if "@apex:end" in line:
                            scope_tag = []

            elif filename.is_dir():
                tag = self.__get_tag(filename.name)
                if tag != "":
                    tags.add(tag)

                var_list = self.__get_vars(filename.name, tag)
                if len(var_list):
                    vars_to_tag.update(var_list)

                tags_tmp, vars_tmp = self.parse_syntax(filename.path)
                tags.update(tags_tmp)
                vars_to_tag.update(vars_tmp)

        return tags, vars_to_tag

    def generate_project(
        self,
        blueprint_dir: str,
        dst_dir: str,
        project_name: str,
        selected_tags: set,
        selected_vars: dict,
    ) -> None:
        """
        Generate project from template

        :param blueprint_dir: blueprint directory
        :param dst_dir: destination directory
        :param project_name: project name
        :param selected_tags: selected tags from template by user
        :param selected_vars: selected variables from template by user
        """

        if os.path.exists(os.path.join(dst_dir, project_name)):
            raise FileExistsError(f"{dst_dir} already exists")
        os.mkdir(os.path.join(dst_dir, project_name))

        self.__iterate_blueprint(
            blueprint_dir,
            os.path.join(dst_dir, project_name),
            selected_tags,
            selected_vars,
        )

    def __iterate_blueprint(
            self,
            blueprint_dir: str,
            dst_dir: str,
            selected_tags: set,
            selected_vars: dict,
    ) -> None:
        """
        Generate files from template and write them to destination directory recursively

        :param blueprint_dir: blueprint directory
        :param dst_dir: destination directory
        :param selected_tags: selected tags from template by user
        :param selected_vars: selected variables from template by user
        """
        for filename in os.scandir(blueprint_dir):
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

                        tag = self.__get_tag(line)
                        if tag != "":
                            if tag not in selected_tags:
                                ignore_flag = True
                            continue

                        var_list = self.__get_vars(line, "")
                        if len(var_list):
                            for var_key in var_list:
                                if var_key in selected_vars:
                                    line = line.replace(f"@apex:{var_key}:var", selected_vars[var_key])
                                else:
                                    raise ValueError(f"Variable {var_key} not found in selected variables")

                        content.append(line)
                self.__write_file(os.path.join(dst_dir, filename.name), content)

            elif filename.is_dir():
                dir_name = filename.name

                tag = self.__get_tag(dir_name)
                if tag != "":
                    if tag not in selected_tags:
                        continue
                    dir_name = dir_name.replace(f"@apex:{tag}:tag", "")

                var_list = self.__get_vars(dir_name, "")
                if len(var_list):
                    for var_key in var_list:
                        if var_key in selected_vars:
                            dir_name = dir_name.replace(f"@apex:{var_key}:var", selected_vars[var_key])
                        else:
                            raise ValueError(f"Variable {var_key} not found in selected variables")

                os.mkdir(os.path.join(dst_dir, dir_name))
                self.__iterate_blueprint(
                    filename.path,
                    os.path.join(dst_dir, dir_name),
                    selected_tags,
                    selected_vars,
                )

    @staticmethod
    def __write_file(path: str, content: List[AnyStr]) -> None:
        """
        Write content to file

        :param path: file path
        :param content: file content
        """
        with open(path, "w") as f:
            f.writelines(content)
