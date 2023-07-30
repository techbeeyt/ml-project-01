from setuptools import find_packages, setup
from typing import List

HYPHEN_E_DOT = '-e .'
def get_requirements(file_path:str)->List[str]:
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n", "") for req in requirements]
        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)
setup(
    name='mlproject',
    version='0.0.1',
    author="Montasir",
    author_email='mmcse19@gmail.com',
    packages=find_packages(),
    install_reuires=get_requirements('requirements.txt')
)