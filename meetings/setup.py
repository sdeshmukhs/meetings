# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in meetings/__init__.py
from meetings import __version__ as version

setup(
	name='meetings',
	version=version,
	description='this is just an example.',
	author='SD',
	author_email='sayali.d@indictranstech.com',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
