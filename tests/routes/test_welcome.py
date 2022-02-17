import json

from tests import BaseTest


class TestWelcome(BaseTest):

    def test_index(self):
        res = self.client.get('/')
        self.assertEqual(200, res.status_code)
