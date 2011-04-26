#!/usr/bin/env python
from distutils.core import setup

setup(
    name='FacebookJavaScriptSDK',
    version='0.1',
    maintainer="Tomasz Wysocki",
    maintainer_email="tomasz@wysocki.info",
    install_requires=(
        'django',
        'django-package-installer',
        'facebook-config',
    ),
    packages=[
        'facebook_javascript_sdk',
        'facebook_javascript_sdk.templatetags',
    ],
)
