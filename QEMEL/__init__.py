from PyQt5.QtQml import qmlRegisterType


def RegisterObjects():
    from .namespace1 import Person
    qmlRegisterType(Person, 'QEMEL.Objects', 1, 0, 'Person')
