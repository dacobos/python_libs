
################################  MODULE  INFO  ################################
# Author: David  Cobos
# Cisco Systems Solutions Integrations Architect
# Mail: cdcobos1999@gmail.com  / dacobos@cisco.com
##################################  IMPORTS   ##################################


# Depends: PyQt4 Library

# Usage Example to select a file:
# from file_helper import *
# f = select('file')
# Or
# f = select('folder')

# Returns: file or folder path

# Un official Windows binaries to install PyQt4 https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyqt4
# In the filenames cp27 means C-python version 2.7, cp35 means python 3.5, etc.
# C:\path\where\wheel\is\> pip install PyQt4-4.11.4-cp35-none-win_amd64.whl

from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4 import QtGui, QtCore
import sys



app=QtGui.QApplication(sys.argv)
result = None

class Widget(QtGui.QWidget):

    def __init__(self):
        super(Widget, self).__init__()
        self.textbox = QLineEdit(self)
        self.result =  None

    def remove_widget(self):
        self.deleteLater()


    def select_file(self):
        global result
        result = QtGui.QFileDialog.getOpenFileName(self,'../' ,'Select File')
        self.textbox.setText(result)
        self.textbox.setReadOnly(1)
        self.textbox.setFrame(1)
        self.textbox.setPlaceholderText("No File Selected Yet")
        self.textbox.setGeometry(50,50,700,30)
        self.button1 = QtGui.QPushButton("Ok",self)
        self.button1.setGeometry(50,100,100,30)
        self.button1.clicked.connect(self.remove_widget)
        self.button2 = QtGui.QPushButton("Select Again",self)
        self.button2.setGeometry(150,100,100,30)
        self.button2.clicked.connect(self.select_file)
        self.setWindowTitle('Selected File')
        self.resize(800, 150)
        qr = self.frameGeometry()
        cp = QtGui.QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
        self.show()


    def select_folder(self):
        global result
        result = QtGui.QFileDialog.getExistingDirectory(self, 'Select Folder')
        self.textbox.setText(result)
        self.textbox.setReadOnly(1)
        self.textbox.setFrame(1)
        self.textbox.setPlaceholderText("No File Selected Yet")
        self.textbox.setGeometry(50,50,700,30)
        self.button1 = QtGui.QPushButton("Ok",self)
        self.button1.setGeometry(50,100,100,30)
        self.button1.clicked.connect(self.remove_widget)
        self.button2 = QtGui.QPushButton("Select Again",self)
        self.button2.setGeometry(150,100,100,30)
        self.button2.clicked.connect(self.select_folder)
        self.setWindowTitle('Selected File')
        self.resize(800, 150)
        qr = self.frameGeometry()
        cp = QtGui.QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
        self.show()

def select(arg):
    window = Widget()

    if arg == 'file':
        window.select_file()
    elif arg == 'folder':
        window.select_folder()
    else:
        pass
    app.exec_()
    print "file_helper.py - result: Selected " + str(result)
    return str(result)

def main():
    arg = raw_input("Select an option (file/folder):")
    if arg == 'file' or arg == 'folder':
        result = select(arg)
        print "You selected: " + result
    else:
        print "That option "+arg+" did't work, you must have written: (file or folder)"
    print "file_helper.py - result: Selected " + str(result)
    return result

if __name__ == "__main__":
    main()
