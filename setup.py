#!/usr/bin/env python

import sys
from setuptools import find_packages, setup

install_requires = [
    'xmltodict',
    'termcolor',
    'setuptools',
    'rosinstall_generator',
    'rosdistro',
    'rosdep',
    'gitpython',
    'requests >= 2.14.0',
    'docker',
    'pyyaml',
    'pygithub',
    'catkin_pkg >= 0.4.0',
    'docker-pycreds',
    'websocket-client',
    'gitdb2',
    'rospkg'
]

setup(
    name='superflore',
    version='0.2.1',
    packages=find_packages(exclude=['tests', 'tests.*']),
    author='Hunter L. Allen',
    author_email='hunter@openrobotics.org',
    url='https://github.com/ros-infrastructure/superflore',
    keywords=['ROS'],
    install_requires=install_requires,
    classifiers=['Programming Language :: Python',
                 'License :: OSI Approved :: Apache Software License'],
    description='Super Bloom',
    license='Apache 2.0',
    test_suite='tests',
    entry_points={
        'console_scripts': [
            'superflore-gen-ebuilds = superflore.generators.ebuild:main',
            'superflore-gen-meta-pkgs = superflore.generators.bitbake:main',
            'superflore-check-ebuilds = superflore.test_integration.gentoo:main',
        ]
    }
)
