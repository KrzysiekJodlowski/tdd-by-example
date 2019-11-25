from test_case import TestCase


class WasRun(TestCase):
    def __init__(self, name):
        TestCase.__init__(self, name)

    def setup(self):
        self.log = "setUp "

    def test_method(self):
        self.log = self.log + "testMethod "

    def tear_down(self):
        self.log = self.log + "tearDown "

    def test_broken_method(self):
        raise Exception
