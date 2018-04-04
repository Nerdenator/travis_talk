from unittest import TestCase

from travis_talk.command_line import main

class TestCmd(TestCase):
    def test_basic(self):
        main()