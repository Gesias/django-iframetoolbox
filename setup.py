#!/usr/bin/python
# -*- coding: UTF-8 -*-
import os
from setuptools import setup, find_packages


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


VERSION='0.2.2'

setup(
    name='django-iframetoolbox',
    version='0.2.2',
    description='Package for handling iframes and sessions.',
    author='Django-iframetoolbox from bitbucket initially.',
    author_email='klas79@gmail.com',
    url='http://example.com',
    packages=['*'],
      long_description="""\
      The rain in spain stays mainly in a plain
      """,
      classifiers=[
          "License :: OSI Approved :: GNU General Public License (GPL)",
          "Programming Language :: Python",
          "Development Status :: 4 - Beta",
          "Intended Audience :: Developers",
          "Topic :: Internet",
      ],
      keywords='internet session handling',
      license='GPL',
      install_requires=[
        'setuptools',
	'django>=1.5'
      ],
      )
