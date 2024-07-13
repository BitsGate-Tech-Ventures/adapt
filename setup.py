from setuptools import setup, find_packages
import os

def read_requirements():
    with open('requirements.txt') as req:
        return req.read().splitlines()

setup(
    name='MyPackage',
    version='0.1',
    packages=find_packages(),
    install_requires=read_requirements(),
    entry_points={
        'console_scripts': [
            'run_notebook = run_notebook:main',
        ],
    },
)