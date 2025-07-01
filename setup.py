from setuptools import find_packages, setup
from typing import List


def get_requirements(file_path: str) -> List[str]:
    """
    This function reads a requirements file and returns a list of packages.
    """
    requirments = []
    with open(file_path) as file:
        requirments = file.readlines()
        requirments = [req.replace("\n", "") for req in requirments]
        if "-e ." in requirments:
            requirments.remove("-e .")

setup(
name = "MINIPROJECTML",
version = "0.1.0",
author = "Nha Le",
author_email = "lethanhnha2507@gmail.com",
packages = find_packages(),
install_requires = get_requirements("requirements.txt"),
)