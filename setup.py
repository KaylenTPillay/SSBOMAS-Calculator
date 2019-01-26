from setuptools import setup, find_packages

setup(
    author='Kaylen Travis Pillay',
    name='SSB-Calculator',
    description='Super Simple BODMAS Calculator',
    packages=find_packages(),
    version='1.0.0',
    entry_points={
        'console_scripts':['ssbc=my_calculator.cli:main']
    }
)