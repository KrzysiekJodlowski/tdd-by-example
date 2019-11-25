from test_case import TestCase


class WasRun(TestCase):
    def __init__(self, name):
        TestCase.__init__(self, name)

    def test_method(self):
        self.was_run = 1

    def setup(self):
        self.was_run = None
        self.was_setup = 1
