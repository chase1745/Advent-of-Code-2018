import sys
import os

def newday(day, problem):
    dirname = '{}-{}'.format(day, problem)
    filename = '{}-{}.py'.format(day, problem)
    os.mkdir(dirname)
    with open(dirname + '/' + filename, 'w+') as f:
        f.write(
            """
import sys
sys.path.append('..')
from adventHelper import FileReader
            """
            )

if __name__ == '__main__':
    newday(sys.argv[1], sys.argv[2])