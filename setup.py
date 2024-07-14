from setuptools import setup, find_packages

def read_requirements():
    with open('requirements.txt') as req:
        return req.read().splitlines()

setup(
    name='mypackage',
    version='0.1',
    packages=find_packages(),
    install_requires=read_requirements(),
    entry_points={
        'console_scripts': [
            'run_notebook = mypackage.run_notebook:main',
        ],
    },
)
