import os
from pathlib import Path

from setuptools import find_packages, setup

this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))
# parse from requirements.txt
install_requires = []
with open('requirements.txt') as f:
    for line in f:
        install_requires.append(line.strip())

setup(
    name='django-firebase-auth',
    version="1.0.3",
    packages=find_packages(),
    install_requires=install_requires,
    url='https://github.com/maycuatroi/django-firebase-auth',
    include_package_data=True,
    license='MIT License',
    description='Django authentication middle ware using Firebase Authentication Service',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Nguyen Anh Binh',
    author_email='sometimesocrazy@gmail.com',
)
