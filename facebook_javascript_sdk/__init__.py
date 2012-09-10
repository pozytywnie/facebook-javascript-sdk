from django.conf.urls.defaults import include
from django.conf.urls.defaults import patterns
from package_installer import Package

class FacebookJavaScriptSDKPackage(Package):
    INSTALL_APPS = ('facebook_javascript_sdk',)
    REQUIRE = ('facebook_config',)

PACKAGE = FacebookJavaScriptSDKPackage()
