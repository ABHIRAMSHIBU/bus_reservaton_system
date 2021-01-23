# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'udp-reciever_gui.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import os
import asyncio
from threading import Thread

from PyQt5.QtCore import QRunnable, pyqtSlot, QThreadPool, QObject, QThread


class Worker(QObject):
    '''
    Worker thread
    '''

    def setAction(self,function):
        self.exec = function


    def run(self):
        self.exec()

class readProcess:
    def __init__(self, process, exec):
        self.p = process
        self.exec = exec
        self.t = Thread(target=self.executionStub)
        self.t.start()

    def executionStub(self):
        p = self.p
        while (True):
            line = p.readline()
            if (not line):
                break
            self.exec(line)


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(567, 629)
        self.flag=True
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(210, 20, 131, 31))
        font = QtGui.QFont()
        font.setFamily("URW Gothic")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(420, 370, 111, 31))
        font = QtGui.QFont()
        font.setFamily("URW Gothic")
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(130, 370, 271, 28))
        self.lineEdit.setObjectName("lineEdit")
        pwd = os.getcwd().replace(" ", "\ ")
        self.lineEdit.setText(pwd + "/testfiles/test.png")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(90, 369, 41, 31))
        font = QtGui.QFont()
        font.setFamily("URW Gothic")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.lineEdit_2 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_2.setGeometry(QtCore.QRect(130, 441, 271, 28))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(100, 440, 21, 31))
        font = QtGui.QFont()
        font.setFamily("URW Gothic")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.lineEdit_3 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_3.setGeometry(QtCore.QRect(130, 511, 271, 28))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_3.setText("5006")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(90, 510, 41, 31))
        font = QtGui.QFont()
        font.setFamily("URW Gothic")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(230, 570, 91, 41))
        font = QtGui.QFont()
        font.setFamily("URW Gothic")
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.portOpener)
        #self.pushButton_2.clicked.connect(self.passSender)
        self.textBrowser = QtWidgets.QTextBrowser(Dialog)
        self.textBrowser.setGeometry(QtCore.QRect(90, 110, 381, 192))
        font = QtGui.QFont()
        font.setFamily("Source Code Pro")
        self.textBrowser.setFont(font)
        self.textBrowser.setObjectName("textBrowser")
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "UDP Sender"))
        self.label.setText(_translate("Dialog", "UDP Sender"))
        self.pushButton.setText(_translate("Dialog", "Browse"))
        self.label_2.setText(_translate("Dialog", "File:"))
        self.label_3.setText(_translate("Dialog", "IP:"))
        self.label_4.setText(_translate("Dialog", "Port:"))
        self.pushButton_2.setText(_translate("Dialog", "Send"))


    def runner(self):
        filedata = self.lineEdit.text()
        hostip = self.lineEdit_2.text()
        if not filedata:
            filedata = "testfiles/test.png"
        if not self.lineEdit_3.text():
            port = 5006
        else:
            port = int(self.lineEdit_3.text())
        if not hostip:
            hostip = "127.0.0.1"
        #self.client = os.system(")
        self.client = os.popen("python udpSenderMain.py --file {0} -up {1} --host {2}".format(filedata, port, hostip))
        exec = lambda data: self.textBrowser.setPlainText(self.textBrowser.toPlainText()+data)
        while (True):
            line = self.client.readline()
            if (not line):
                break
            exec(line)

    def portOpener(self):
        if self.flag:
            self.thread = QThread()
            self.worker = Worker()
            self.worker.setAction(self.runner)
            self.thread.started.connect(self.worker.run)
            self.thread.start()
            self.pushButton_2.setText("Close")
            self.flag = False
        else:
            exit(0)
        # self.runner()
        # worker = Worker()
        # worker.setAction(self.runner)
        # self.threadpool.start(worker)

        # serverReader  = readProcess(self.server,exec)


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
