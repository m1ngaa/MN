# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in mn/__init__.py
from mn import __version__ as version

setup(
	name='mn',
	version=version,
	description='MN-izing for personal use',
	author='Manduul B.',
	author_email='manduul@hello.mn',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
