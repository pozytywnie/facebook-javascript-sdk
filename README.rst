facebook-javascript-sdk
========================

facebook-javascript-sdk is a Django application that provides
a template tag for including Facebook asynchronous JavaScript SDK.

Installation
------------

Package
_______

facebook-javascript-sdk can be installed as normal Python package.

Example installation for pip::

    $ pip install facebook-javascript-sdk

Example installation from file::

    $ pip install facebook-javascript-sdk-1.0.tar.gz

Configuration
-------------

settings.py
___________

Add facebook_javascript_sdk to INSTALLED_APPS::

    INSTALLED_APPS = (
        ...
        'facebook_javascript_sdk',
        ...
    )

Set your Facebook application ID under FACEBOOK_APP_ID variable::

    FACEBOOK_APP_ID = 12345

template
________

Add fb_init_block tag in the BODY section of your page template::

    {% load facebook_javascript_sdk %}
    {% fb_init_block %}{% endblock %}

Usage
-----

The {% fb_init_block %}{% endblock %} will load the SDK and you can use it in your JS files.
If you want to execute some code after SDK gets loaded you can put the code inside the block::

    {% fb_init_block %}
    FB.getLoginStatus(function(response) {
        if (response.status === 'connected') {
            isAuthenticated = true;
            login(response.authResponse.accessToken, yourCallbackFunction);
        }
    });
    {% endblock %}
