import os
import sys
from PyQt5.QtQml import QQmlExtensionPlugin, qmlRegisterType

THIS_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(THIS_DIR, "..", ".."))
from QEMEL.namespace1 import Person

class QEMELPlugin(QQmlExtensionPlugin):

    def registerTypes(self, uri):
        qmlRegisterType(Person, uri, 1, 0, 'Person')

    def initializeEngine(self, engine, uri):
        qmlRegisterType(Person, 'QEMEL.Objects', 1, 0, 'Person')
