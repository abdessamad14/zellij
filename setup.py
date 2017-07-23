#!/usr/bin/env python3

from setuptools import setup

setup(
    name='zellij',
    version='0.1.0',
    license='MIT',
    description='Islamic tiling toy',
    author='Ned Batchelder',
    author_email='ned@nedbatchelder.com',
    url='https://github.com/nedbat/zellij',
    packages=['zellij'],
    zip_safe=True,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
    ],
)