__author__ = 'agupt15'

import ftplib


print('Trying connection...')

UAT = '10.193.19.247', 'OFFICE\acai03', 'Iveymsc2014'
LOCALHOST = '127.0.0.1', "admin", 'bmo123'
DEBUG_LEVEL = 2

WORKING_HOST = UAT
with ftplib.FTP(host=WORKING_HOST[0], timeout=None) as ftp:
    print('Trying host {0}'.format(WORKING_HOST[0]))
    ftp.set_debuglevel(DEBUG_LEVEL)
    ftp.login(user=WORKING_HOST[1], passwd=WORKING_HOST[2])
    print('Login Status')

    print(ftp.dir())