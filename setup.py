from setuptools import setup , find_packages
from typing import List

def get_requirements(file_path:str)->List[str]:
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines
        requirements = [req.replace("\n","") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    return requirements

setup(
    name = 'DiamondPricePrediction',
    version='0.1',
    author='Harshit',
    author_email='srivastavh98@gmail.com',
    install_requirement = get_requirements("requirements.txt"),
    packages=find_packages
)