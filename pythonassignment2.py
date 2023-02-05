

class Logger:

    def __init__(self):
        self.msg ={}

    def shouldPrintMessage(self, timestamp, message):

        if message not in self.msg:
            self.msg[message] = timestamp
            return True

        if self.msg[message] + 10 <= timestamp:
            self.msg[message] = timestamp
            return True
        else:
            return False

logger = Logger()

print(logger.shouldPrintMessage(10, "foo"))