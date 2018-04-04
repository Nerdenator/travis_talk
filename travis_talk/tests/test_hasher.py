from unittest import TestCase

import travis_talk

class TestTravis(TestCase):
    def test_output(self):
        s = travis_talk.hash_string()
        self.assertEqual(s, "28ce06092bd2a57fa5804a5611a38533")