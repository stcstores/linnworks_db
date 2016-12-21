#!/usr/bin/env python

from setuptools import setup, find_packages

setup(
    name='linnworks_db',
    version='1.0',
    description='Container for Linnworks related Databases',
    author='Luke Shiner',
    author_email='luke@lukeshiner.com',
    packages=find_packages(),
    install_requires=[
        'pydatabase',
    ])
