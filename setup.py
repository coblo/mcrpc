#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import setup, find_packages


def readme():
    with open('README.rst') as f:
        return f.read()


setup(
    name='mcrpc',
    version='0.2.5',
    description="mcrpc: MultiChain RPC Library",
    long_description=readme(),
    author="Titusz Pan",
    author_email='tp@py7.de',
    url='https://github.com/coblo/mcrpc',
    packages=find_packages(include=['mcrpc']),
    include_package_data=True,
    install_requires=['requests', 'simplejson'],
    license="GNU General Public License v3",
    zip_safe=False,
    keywords="mcrpc, multichain, rpc, client, api, library",
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
    ],
    test_suite='tests',
)
