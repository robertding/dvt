#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re
from setuptools import setup, find_packages


def find_version(fname):
    """Attempts to find the version number in the file names fname.
    Raises RuntimeError if not found.
    """
    version = ''
    with open(fname, 'r') as fp:
        reg = re.compile(r'__version__ = [\'"]([^\'"]*)[\'"]')
        for line in fp:
            m = reg.match(line)
            if m:
                version = m.group(1)
                break
    if not version:
        raise RuntimeError('Cannot find version information')
    return version


__version__ = find_version('dvt/__init__.py')


def read(fname):
    with open(fname) as fp:
        content = fp.read()
    return content


setup(
    name='dvt',
    version=__version__,
    description=(),
    long_description=read('README.md'),
    author='robertding',
    author_email='robertdingx@gmail.com',
    url='https://github.com/robertding/dvt',
    packages=find_packages(exclude=('test*', 'examples')),
    package_dir={'dvt': 'dvt'},
    include_package_data=True,
    extras_require={'reco': {}},
    license='MIT',
    zip_safe=False,
    keywords=(),
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
    ],
    test_suite='tests',
    project_urls={
    },
)
