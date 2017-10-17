from PyQt5.QtQml import qmlRegisterType


def RegisterObjects():
    from .namespace1 import Person
    qmlRegisterType(Person, 'QEMEL', 1, 0, 'Person')
