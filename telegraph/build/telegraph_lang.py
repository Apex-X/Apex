import os
import re
from typing import Tuple, Set, Dict


def parse_telegraph_annotations(tmp_dir: str) -> Tuple[Set[str], Dict[str, str]]:
    """
    Parse telegraph annotations from template

    :param tmp_dir: template directory
    :return: tags, variables
    """
    tags = set({})
    vars = {}
    for filename in os.scandir(tmp_dir):
        if filename.is_file():
            with open(filename.path, "r") as f:
                scope_tag = ""
                for line in f.readlines():
                    tag = get_tag(line)
                    if tag != "" and tag not in tags:
                        tags.add(tag)
                        scope_tag = tag

                    var_list = get_vars(line, scope_tag)
                    if len(var_list):
                        vars.update(var_list)

                    if "@telegraph:end" in line:
                        scope_tag = []

        elif filename.is_dir():
            tag = get_tag(filename.name)
            if tag != "":
                tags.add(tag)
            var_list = get_vars(filename.name, tag)
            if len(var_list):
                vars.update(var_list)
            tags_tmp, vars_tmp = parse_telegraph_annotations(filename.path)
            tags.update(tags_tmp)
            vars.update(vars_tmp)

    return tags, vars


def get_vars(text: str, scope_tag: str) -> Dict[str, str]:
    """
    Get variables from input text

    :param text: text to parse
    :param scope_tag: tag of variable
    :return: variables
    """
    vars = {}
    var_regex = re.compile(r"@telegraph:\w+:var")
    if var_regex.findall(text):
        var_list = var_regex.findall(text)
        for var in var_list:
            if var and var not in vars:
                var = var.split(":")[1]
                vars[var] = scope_tag
    return vars


def get_tag(text: str) -> str:
    tag_regex = re.compile(r"@telegraph:\w+:tag")
    if tag_regex.findall(text):
        tag = tag_regex.findall(text)[0]
        tag = tag.split(":")[1]
        return tag
    return ""
