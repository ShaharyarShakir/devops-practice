from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()
    

REQUIRED_PACKAGES=['numpy','pandas', 'scikit-learn', 'mlflow', 'fastapi', 'pydantic', 'pytest'] 
setup(name='telco-customer', version = '0.1dev', author = "Shaharyar Shakir", packages=find_packages(), long_description=long_description, install_requires=REQUIRED_PACKAGES)  