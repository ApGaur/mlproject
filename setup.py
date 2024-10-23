from setuptools import setup, find_packages
from typing import List

HYPEN_E_DOT='-e .'  # Changed from 'e .' to '-e .'

def get_requirements(file_path:str)->List[str]:
    '''
    This function will return list of requirements
    '''
    requirements=[]
    try:
        with open(file_path) as file_obj:
            requirements=file_obj.readlines()
            requirements=[req.replace("\n",'').strip() for req in requirements]
            
            if HYPEN_E_DOT in requirements:
                requirements.remove(HYPEN_E_DOT)
            
            return [req for req in requirements if req and not req.startswith('#')]
    except FileNotFoundError:
        print(f"Error: {file_path} not found")
        return []

setup(
    name='mlproject',
    version='0.0.1',
    author='Apoorv',
    author_email='agaur004@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)