#!/usr/bin/env python
from distutils.core import setup

setup(
    name='facebook-javascript-sdk',
    version='1.0',
    maintainer="Tomasz Wysocki",
    maintainer_email="tomasz@wysocki.info",
    install_requires=(
        'django',
        'django-package-installer',
        'ludibrio',
        'facebook-config',
    ),
    packages=[
        'facebook_javascript_sdk',
        'facebook_javascript_sdk.templatetags',
    ],
)
