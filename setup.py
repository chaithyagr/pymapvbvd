#!/usr/bin/env python

import setuptools
import versioneer
import yaml

with open("README.md", "r") as fh:
    long_description = fh.read()

with open("requirements.yml", "r") as stream:
    try:
        requirements = yaml.safe_load(stream)
        install_requires = requirements['dependencies']
    except yaml.YAMLError as exc:
        print(exc)

# A horrible hack -  I can't get the requirements.yml to work
# with the dataclass dependency for 3.6
index = install_requires.index('dataclasses')
install_requires[index] += "  ; python_version<'3.7'"

setuptools.setup(
    name='pyMapVBVD',
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    description='Python twix file reader',
    author='Will Clarke',
    author_email='william.clarke@ndcn.ox.ac.uk',
    url='https://github.com/wtclarke/pymapvbvd',
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    install_requires=install_requires,
    license_file='LICENSE',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent", ],
    python_requires='>=3.6')
