from setuptools import find_packages,setup
from typing import List 

HYPEN_E_DOT= '-e .'

def get_requirements(file_path): # getting the file path as a string and mentioning that it will return as a list 
    # creating an empty list 
    requirements = []
    # opening the file with the open function and file as an object 
    with open( file_path)as file:
        # inserting the values into the empty line by line using .readlines functionality 
        requirements= file.readlines()
        
        # replacing the '\n' with " " and returning only the libraries from requirements.txt

        requirements= [req.replace('\n'," ")for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

    return requirements

setup( 
    name = "source",
    version = "0.0.1",
    author = "Pankaj Singh",
    author_email= 'singh.pankaj0018@gmail.com',
    install_requires = get_requirements('requirements.txt'), 
    packages= find_packages()

)