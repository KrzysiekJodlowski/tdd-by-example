from test_case import TestCase
from was_run import WasRun


class TestCaseTest(TestCase):

    def test_template_method(self):
        test = WasRun("test_method")
        test.run()
        assert ("setUp testMethod tearDown " == test.log)


TestCaseTest("test_template_method").run()
