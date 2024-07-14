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
            'run_notebook = mypackage.poc_model_ver_2:main',
        ],
    },
    package_data={
        'mypackage': ['nmap_commands_updated.json', 'nmap_command_classifier.pkl'],
    },
)
