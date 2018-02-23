
################################  MODULE  INFO  ################################
# Author: David  Cobos
# Cisco Systems Solutions Integrations Architect
# Mail: cdcobos1999@gmail.com  / dacobos@cisco.com
##################################  IMPORTS   ##################################


# Usage:
# Argument: logfile.log path

# Instance an object from the class Logger to the sys.stdout: sys.stdout = Logger(../logfile.log)
# To Clear the Log use: sys.stdout.clear(../logfile.log)

import sys
from date_helper import *

class Logger(object):
    def __init__(self, LOG_FILE):
        self.terminal = sys.stdout
        self.log = open(LOG_FILE, "a")

    def clear(self, LOG_FILE):
        open(LOG_FILE, 'w').close()

    def write(self, message):
        self.terminal.write(message)
        self.log.write(GetDateString()+" ")
        self.log.write(message + " ")
        self.log.flush()

    def flush(self):
        #this flush method is needed for python 3 compatibility.
        #this handles the flush command by doing nothing.
        #you might want to specify some extra behavior here.
        pass
