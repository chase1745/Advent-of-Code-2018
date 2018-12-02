import sys
import os

def newProblem(day, problem):
    dirname = '{}-{}'.format(day, problem)
    filename = '{}-{}.py'.format(day, problem)
    os.mkdir(dirname)
    os.rename(os.path.expanduser('~') + '/Downloads/{}-{}.txt'.format(day, problem), dirname + '/{}-{}.txt'.format(day, problem))
    with open(dirname + '/' + filename, 'w+') as f:
        f.write(
            """
import sys
sys.path.append('..')
from adventHelper import FileReader
            """
            )

if __name__ == '__main__':
    newProblem(sys.argv[1], sys.argv[2])