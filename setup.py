#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
sentry-Wetchat-prod
==============

An extension for Sentry which integrates with qy-Wetchat. It will send
notifications to qy-wetchat robot.

:copyright: (c) 2019 by jerry hu, see AUTHORS for more details.
:license: MIT, see LICENSE for more details.
"""

from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="sentry-wechat-prod",
    version='0.1.2',
    author='jerry hu',
    author_email='jerryhu_123@163.com',
    url='https://github.com/5356/sentry-wechat-prod',
    description='A Sentry extension which integrates with Wechat robot.',
    long_description=long_description,
    long_description_content_type="text/markdown",
    license='MIT',
    keywords='sentry wechat',
    include_package_data=True,
    zip_safe=False,
    package_dir={'': 'src'},
    packages=find_packages('src'),
    install_requires=[
        'sentry>=9.0.0',
        'requests',
    ],
    entry_points={
        'sentry.plugins': [
            'wechat_prod = sentry_wechat_prod.plugin:WechatProdPlugin'
        ]
    },
    classifiers=[
        'Programming Language :: Python :: 2.7',
        "License :: OSI Approved :: MIT License",
    ]
)
