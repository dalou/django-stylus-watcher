from __future__ import print_function
import ast
import os
import sys
from fnmatch import fnmatchcase
from distutils.util import convert_path
from setuptools import setup, find_packages

f = open(os.path.join(os.path.dirname(__file__), 'README.rst'))
readme = f.read()
f.close()

setup(
    name='django-stylus-watcher',
    version="1.0",
    description='Django stylus watchers & auto compilers',
    long_description=readme,
    author='Frank Wiles',
    author_email='frank@revsys.com',
    url='http://github.com/dalou/django-stylus-watcher',
    packages=find_packages(),
    zip_safe=False,
    license='MIT',
    classifiers=[
        'Development Status :: 1.0',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Django',
    ],
    test_suite='runtests.runtests',
    install_requires=[
        'watchdog >= 0.8.3',
        'stylus >= 0.1.1',
    ],
)
