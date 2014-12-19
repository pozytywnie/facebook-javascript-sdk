from django.conf import settings as project_settings
from django import template

register = template.Library()


class FbInitNode(template.Node):
    def __init__(self, script, app_id, api_version, *args, **kwargs):
        super(FbInitNode, self).__init__(*args, **kwargs)
        self.script, self.app_id = script, app_id
        self.api_version = api_version

    def render(self, context):
        language_code = context.get('FACEBOOK_LANGUAGE_CODE', 'pl_PL')
        return """
        <div id="fb-root"></div>
        <script type="text/javascript">
          window.fbAsyncInit = function() {
            FB.init({version:'%(version)s', appId: '%(id)s', status: true, cookie: true, xfbml: true});
            (function() {
                %(script)s
            })();
          };
          (function() {
            var e = document.createElement('script'); e.async = true;
            e.src = document.location.protocol +
              '//connect.facebook.net/%(lang)s/sdk.js';
            document.getElementById('fb-root').appendChild(e);
          }());
        </script>
        """ % dict(version=self.api_version, id=self.app_id,
                   script=self.script.render(context), lang=language_code)


@register.tag
def fb_init_block(parser, token, settings=project_settings):
    """
    Asynchronously loads Facebook JavaScript SDK and then executes code in block.

    Use in <body> section only.

    Usage::

        {% fb_init_block %} alert('Facebook SDK loaded'); {% endblock %}
    """
    script = parser.parse(('endblock',))
    parser.delete_first_token()
    version = 'v%s' % getattr(settings, 'FACEBOOK_API_VERSION', '2.1')
    return FbInitNode(script, app_id=settings.FACEBOOK_APP_ID,
                      api_version=version)
