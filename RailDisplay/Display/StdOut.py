# Dummy display used for testing
class StdOut:

    def __init__(self, rail, config=None):
        self.rail = rail
        self.config = config

    @staticmethod
    def display_message(message):
        print message

    @staticmethod
    def alert_late():
        print "Train Late!!!"
