class TestCase:
    def __init__(self, name):
        self.name = name

    def setup(self):
        pass

    def tear_down(self):
        pass

    def run(self, result):
        result.test_started()
        self.setup()
        try:
            method = getattr(self, self.name)
            method()
        except:
            result.test_failed()
        self.tear_down()

