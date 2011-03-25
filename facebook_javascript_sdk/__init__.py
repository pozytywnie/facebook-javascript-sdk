from django.conf.urls.defaults import patterns, include
from package_installer import Package

class FacebookJavaScriptSDKPackage(Package):
    INSTALL_APPS = ('facebook_javascript_sdk')

PACKAGE = FacebookJavaScriptSDKPackage()
