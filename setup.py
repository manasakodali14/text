from setuptools import find_packages,setup
from typing import List

HYPEN='-e .'
SRC_REPO = "textSummarizer"

def get_requirements(file_path:str)->List[str]:
    '''
    this function will return the list of requirements
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        for req in requirements:
            requirements=req.replace("\n","")

        if HYPEN in requirements:
            requirements.remove(HYPEN)
    
    return requirements

setup(
name=SRC_REPO,
version='0.0.0',
author='Manasa',
package_dir={"": "src"},
packages=find_packages(where="src")
#install_requires=get_requirements('requirements.txt')

)