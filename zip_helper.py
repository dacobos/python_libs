# Rev: BETA Under Review

################################  MODULE  INFO  ################################
# Author: David  Cobos
# Cisco Systems Solutions Integrations Architect
# Mail: cdcobos1999@gmail.com  / dacobos@cisco.com
##################################  IMPORTS   ##################################

import os
import zipfile

# Usage:
# from zip_helper import zipper
# zipper(/home/username/folder)

# Depends:
# zipfile library
# Arguments:
# path: full path of folder of file to be commpressed

#Returns:
# Full path and name of zip file


def zipper(path):
    try:
        pwd = os.getcwd()
        root = None
        lis = []
        if os.path.isdir(path):
            filename = os.path.split(path)[1] + ".zip"
            folder = path
        else:
            filename = os.path.split(path)[1]
            folder = os.path.split(path)[0]

        for root, dirs, files in os.walk(folder):
            for file in files:
                os.chdir(root)
                lis.append(file)
        print "Creating file: "+filename
        zipf = zipfile.ZipFile(filename, 'w', zipfile.ZIP_DEFLATED)
        for i in lis:
            print "Adding file: "+i
            if i != filename:
                zipf.write(i)
        print "Completed"
        zipf.close()
        os.chdir(root)
    except:
        print "Something wen't wrong, couln't complete the file"
        os.chdir(root)
    return filename

# zipper(results_folder,filename)
