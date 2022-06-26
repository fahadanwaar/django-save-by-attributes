from setuptools import find_packages, setup
setup(
    name='djangosavebyattributes',
    packages=find_packages(include=['djangosavebyattributes']),
    version='0.1.0',
    description='My first Python library',
    author='Me',
    license='MIT',
    install_requires=["Django"],
)