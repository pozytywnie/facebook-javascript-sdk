#!/usr/bin/env python
from setuptools import setup

setup(
    name='facebook-javascript-sdk',
    version='1.1',
    maintainer="Tomasz Wysocki",
    maintainer_email="tomasz@wysocki.info",
    install_requires=(
        'django',
    ),
    tests_require=(
        'ludibrio',
    ),
    packages=[
        'facebook_javascript_sdk',
        'facebook_javascript_sdk.templatetags',
    ],
)
