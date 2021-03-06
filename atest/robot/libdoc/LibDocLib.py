import os
import tempfile
from os.path import join, dirname, abspath
from subprocess import call, STDOUT

from robot.api import logger
from robot.utils import decode_output

ROBOT_SRC = join(dirname(abspath(__file__)), '..', '..', '..', 'src')

class LibDocLib(object):

    def __init__(self, interpreter):
        self._interpreter = interpreter
        self._cmd = [interpreter, '-m', 'robot.libdoc']

    def run_libdoc(self, args):
        cmd = self._cmd + [a for a in args.split(' ') if a]
        cmd[-1] = cmd[-1].replace('/', os.sep)
        logger.info(' '.join(cmd))
        stdout = tempfile.TemporaryFile()
        call(cmd, cwd=ROBOT_SRC, stdout=stdout, stderr=STDOUT, shell=os.sep=='\\')
        stdout.seek(0)
        output = stdout.read().replace('\r\n', '\n')
        logger.info(output)
        return decode_output(output)
