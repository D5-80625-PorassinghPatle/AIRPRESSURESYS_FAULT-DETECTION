## this is to use this source code as library 
from setuptools import find_packages,setup

from typing import List

REQUIREMENT_FILE_NAME="requirements.txt"
HYPEN_E_DOT="-e ."

def get_requirements():

    with open(REQUIREMENT_FILE_NAME) as requirement_file:

        requiremnet_list=requirement_file.readlines()

    requiremnet_list=[x.replace("\n","") for x in requiremnet_list]

    if HYPEN_E_DOT in  requiremnet_list:

        requiremnet_list.remove(HYPEN_E_DOT)

    return requiremnet_list


setup(
    name="sensor",
    version="0.0.3",
    author="poras",
    author_email="poraspatle@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements()

)