# This script is used to package and distribute a Python project using setuptools. 
# That means it defines metadata about the project, its dependencies, and other configuration details needed for installation.
from typing import List
from setuptools import find_packages, setup

HYPEN_E_DOT = '-e .'
def get_requirements(file_path: str) -> List[str]:
    """This function returns the list of requirements"""
    requirements = []
    with open(file_path, 'r') as file:
        requirements = file.readlines()
        requirements = [req.replace('\n', '') for req in requirements]
    
    if HYPEN_E_DOT in requirements:
        requirements.remove(HYPEN_E_DOT)
    
    return requirements


setup(
    name='my_python_project',
    version='0.1.0',
    author='Phuong Huong Nguyen',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)