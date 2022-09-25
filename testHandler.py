from sqlConnectors import get_tests


class Test():
    def __init__(self,frame):
        self.frame=frame
        self.tests = get_tests()

    def returnTests(self):
        return self.tests

