#!/usr/bin/python

from PyQt4 import QtGui
from guimessages import translations


class gui_message(QtGui.QMessageBox):
    def __init__(self, filename, section):
        super(gui_message, self).__init__()

        tr = translations._translations(filename, section)
        self.icon = tr.section.get('icon')
        self._ = tr.gettext
        self.initUI()

    def initUI(self):
        self.setWindowIcon(QtGui.QIcon("/usr/share/icons/anon-icon-pack/whonix.ico"))
        self.setIcon(getattr(QtGui.QMessageBox, self.icon))
        self.setWindowTitle(self._('title'))
        self.setText(self._('message'))
        self.exec_()
