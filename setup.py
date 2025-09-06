'''
The setup.py file is an essential part of packaging and distributing python project.
It is used by setuptools (or distutils in older python version) to define the configuration
of your project , such as its metadata, dependencies and more...
'''

from setuptools import find_packages, setup
from typing import List

def get_requirements()->List[str]:
    """
    this function will return lst of requirements
    """
    requirement_lst:List[str]=[]
    try:
        with open('requirements.txt', 'r') as file:
            #Read lines from the file
            lines = file.readlines()
            # Proces each lines
            for line in lines:
                requirement= line.strip()
                ##ignore empty lines and -e .
                if requirement and requirement!= '-e .':
                    requirement_lst.append(requirement)
    except FileNotFoundError:
        print("requirements.txt is not found")
    
    return requirement_lst

setup(
    name="NetworkSecurity",
    version = "0.0.1",
    author ="Harshil",
    author_email ="solankiharshil058@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements()
)