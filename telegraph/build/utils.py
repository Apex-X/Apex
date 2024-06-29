from enum import Enum
import tempfile
import requests
import tarfile
import os


class VSCType(Enum):
    GitHub = "github"
    GitLab = "gitlab"


def get_template(git_token: str, vcs_type: str, template_id: int) -> tempfile.TemporaryDirectory:
    """
    Get template from VCS

    :param git_token: token for git
    :param vcs_type: VCS type (Github or Gitlab)
    :param template_id: id of template repository in VCS
    :return: template directory
    """
    temp_dir = tempfile.TemporaryDirectory(prefix="telegraph")

    # TODO: add costume VCS link
    if vcs_type == VSCType.GitHub.value:
        # TODO: implement for github
        raise Exception("not implemented")
    elif vcs_type == VSCType.GitLab.value:
        headers = {"Private-Token": git_token}
        url = f"https://gitlab.snapp.ir/api/v4/projects/{template_id}/repository/archive.tar.gz?ref=main"
        response = requests.get(
            url,
            headers=headers,
        )
    else:
        raise Exception("not implemented")

    with open(os.path.join(temp_dir.name, "archive.tar.gz"), "+wb") as f:
        f.write(response.content)

    tar = tarfile.open(os.path.join(temp_dir.name, "archive.tar.gz"), 'r')
    tar.extractall(temp_dir.name)
    tar.close()

    os.remove(os.path.join(temp_dir.name, "archive.tar.gz"))

    return temp_dir

