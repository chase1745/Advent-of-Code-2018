class FileReader():
    def __init__(self, day, problem):
        self.filename = 'day{}-{}.txt'.format(day, problem)

    def getlines(self):
        with open(self.filename, 'r') as f:
            for line in f:
                yield line        