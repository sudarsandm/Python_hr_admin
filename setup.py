from setuptools import setup, find_packages

with open('README.rst', 'r') as f:
    readme = f.read()

setup(
    name='hr',
    version='0.1.0',
    description='Commandline user management utility',
    long_description=readme,
    author='Sudarsan Devarajulu',
    author_email='sudarsandm@gmail.com',
    packages=find_packages('src'),
    package_dir={'':'src'},
    install_requires=[]
)
