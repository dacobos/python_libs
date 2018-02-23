
################################  MODULE  INFO  ################################
# Author: David  Cobos
# Cisco Systems Solutions Integrations Architect
# Mail: cdcobos1999@gmail.com  / dacobos@cisco.com
##################################  IMPORTS   ##################################


import datetime

def GetDateString():
    date_format = '%d/%m/%Y-%H:%M:%S'
    now = datetime.datetime.now()
    this_date = now.strftime(date_format)
    return this_date
