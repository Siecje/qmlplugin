import os
import sys
from PyQt5.QtQml import QQmlExtensionPlugin

THIS_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(THIS_DIR, "..", ".."))
import QEMEL

class QEMELPlugin(QQmlExtensionPlugin):

    def registerTypes(self, uri):
        QEMEL.RegisterObjects()
        with open('/home/siecje/what', 'a') as logFile:
            logFile.write("after register\n\n")
