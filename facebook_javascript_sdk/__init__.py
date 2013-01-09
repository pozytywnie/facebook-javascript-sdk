from django.conf.urls import include
from django.conf.urls import patterns
from package_installer import Package


class FacebookJavaScriptSDKPackage(Package):
    INSTALL_APPS = ('facebook_javascript_sdk',)
    REQUIRE = ('facebook_config',)

PACKAGE = FacebookJavaScriptSDKPackage()
