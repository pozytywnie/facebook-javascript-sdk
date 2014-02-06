#!/usr/bin/env python
from distutils.core import setup

setup(
    name='facebook-javascript-sdk',
    version='1.1',
    maintainer="Tomasz Wysocki",
    maintainer_email="tomasz@wysocki.info",
    install_requires=(
        'django',
        'django-package-installer',
        'facebook-config',
    ),
    tests_require=(
        'ludibrio',
    ),
    packages=[
        'facebook_javascript_sdk',
        'facebook_javascript_sdk.templatetags',
    ],
)
