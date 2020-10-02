#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup

with open('README.md') as readme_file:
    readme = readme_file.read()

requirements = [
    'opencv-python',
    'numpy',
    'pathlib'
]

test_requirements = [
    'tox',
    'flake8'
]

setup(
    name='matrix_rotation',
    version='0.1',
    description="Rotate any square matrix clockwise and anticlockwise in any degree.",
    long_description=readme,
    author="Vaibhav Hiwase",
    author_email='hiwase.vaibhav@gmail.com',
    url='https://github.com/vhiwase/matrix-rotation',
    packages=[
        'matrix_rotation',
    ],
    package_dir={'matrix_rotation': 'matrix_rotation'},

    entry_points={
        'console_scripts': [
            'matrix_rotation=matrix_rotation.matrix_rotation_cli:main'
        ]
    },
    install_requires=requirements,
    license="MIT license",
    zip_safe=False,
    keywords='matrix_rotation',
    classifiers=[
        'Development Status :: 0.2 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    test_suite='tests',
    tests_require=test_requirements
)
