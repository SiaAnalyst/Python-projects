from setuptools import setup, find_packages

setup(
    name='clean_folder',
    version='1.0',
    description='sorting folders script',
    long_description=open('README.md').read(),
    url='https://github.com/SiaAnalyst/Python-projects',
    author='SIA',
    packages=find_packages(),
    license='MIT',
    entry_points={'console_scripts': ['clean_folder = clean_folder.main:clean_folder']}
)
