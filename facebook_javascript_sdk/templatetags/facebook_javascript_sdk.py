from django import template
from django.conf import settings as project_settings

register = template.Library()

class FbInitNode(template.Node):
    def __init__(self, script, app_id, *args, **kwargs):
        super(FbInitNode, self).__init__(*args, **kwargs)
        self.script, self.app_id = script, app_id
    def render(self, context):
        return """
        <div id="fb-root"></div>
        <script type="text/javascript">
          window.fbAsyncInit = function() {
            FB.init({appId: '%(id)s', status: true, cookie: true, xfbml: true});
            (function() {
                %(script)s
            })();
          };
          (function() {
            var e = document.createElement('script'); e.async = true;
            e.src = document.location.protocol +
              '//connect.facebook.net/pl_PL/all.js';
            document.getElementById('fb-root').appendChild(e);
          }());
        </script>
        """ % dict(id=self.app_id, script=self.script.render(context))

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
    return FbInitNode(script, app_id=settings.FACEBOOK_APP_ID)
