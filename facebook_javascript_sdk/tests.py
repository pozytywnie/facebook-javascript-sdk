from django.test import TestCase
from ludibrio import Dummy
from ludibrio import Stub

from facebook_javascript_sdk.templatetags.facebook_javascript_sdk import fb_init_block


# pylint: disable=W0104, W0106
class FbInitTagTest(TestCase):
    def test_settings_cary_over(self):
        test_script = "test_script();"
        app_id = "1235"
        with Stub() as parser:
            parser.delete_first_token()
            parser.parse(('endblock',)).render(Dummy()) >> test_script
        with Stub() as settings:
            settings.FACEBOOK_APP_ID >> app_id
        node = fb_init_block(parser, Dummy(), settings=settings)
        content = node.render(Dummy())
        self.assertNotEqual(-1, content.find(test_script))
        self.assertNotEqual(-1, content.find(app_id))
