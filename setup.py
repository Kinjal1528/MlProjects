# Helps me create the ML application as a package 
# we can also upload this package to PyPI and install it using pip
from setuptools import find_packages, setup
from typing import List

HYPHEN_E_DOT='-e .'
def get_requirements(file_path:str)->List[str]:
    '''
    this fn will return the list of requirements
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","")for req in requirements] 
        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)
        
    return requirements

# meta data info about my ML package goes here in Setup
setup(
    name="mlProject",
    version="0.0.1",
    author="Kinjal",
    author_email="kinjal.workmail@gmail.com",
    packages=find_packages(),#when this runs it will search for the location where __init__.py exists and it will consider the source as package and then it will try to build it, but we will habe to put it in Pypi package  
    install_requires=get_requirements('requirements.txt')
)