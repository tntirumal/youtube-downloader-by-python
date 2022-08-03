# -*- coding: utf-8 -*-

'''
Author: T.N.Tirumal
Title: GUI youtube downloader
'''


from PyQt5 import QtCore, QtGui, QtWidgets
import threading
from pytube import YouTube
from pytube.cli import on_progress,display_progress_bar
import os

global yt

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(640, 480)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../download.jpeg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(120, 30, 361, 31))
        self.label.setTextFormat(QtCore.Qt.RichText)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(70, 110, 67, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setTextFormat(QtCore.Qt.PlainText)
        self.label_2.setObjectName("label_2")
        
        self.LinkBox = QtWidgets.QLineEdit(Dialog)
        self.LinkBox.setGeometry(QtCore.QRect(150, 110, 341, 31))
        self.LinkBox.setObjectName("LinkBox")
        
        self.audio = QtWidgets.QRadioButton(Dialog)
        self.audio.setGeometry(QtCore.QRect(160, 170, 112, 23))
        self.audio.setObjectName("audio")
        self.video = QtWidgets.QRadioButton(Dialog)
        self.video.setGeometry(QtCore.QRect(370, 170, 112, 23))
        self.video.setObjectName("video")

        self.submit = QtWidgets.QPushButton(Dialog)
        self.submit.setGeometry(QtCore.QRect(270, 230, 89, 25))
        self.submit.setStyleSheet("background-color:rgb(87, 227, 137)")
        self.submit.setDefault(True)
        self.submit.setObjectName("submit")
        self.submit.clicked.connect(self.video_down)
        
        self.exit = QtWidgets.QPushButton(Dialog)
        self.exit.setGeometry(QtCore.QRect(500, 390, 89, 25))
        self.exit.setAutoFillBackground(False)
        self.exit.setStyleSheet("background-color:rgb(224, 27, 36)")
        self.exit.setDefault(True)
        self.exit.setObjectName("exit")
        self.exit.clicked.connect(self.closeEvent)

        self.groupBox = QtWidgets.QGroupBox(Dialog)
        self.groupBox.setGeometry(QtCore.QRect(130, 290, 311, 80))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Condensed")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox.setFont(font)
        self.groupBox.setFocusPolicy(QtCore.Qt.TabFocus)
        self.groupBox.setAutoFillBackground(True)
        self.groupBox.setObjectName("groupBox")
        self.progressBar = QtWidgets.QProgressBar(self.groupBox)
        self.progressBar.setGeometry(QtCore.QRect(0, 50, 301, 23))
        self.progressBar.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.progressBar.setAutoFillBackground(False)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.TITLE = QtWidgets.QLabel(self.groupBox)
        self.TITLE.setGeometry(QtCore.QRect(10, 30, 461, 17))
        self.TITLE.setObjectName("TITLE")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Youtube downloader"))
        self.label.setToolTip(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:20pt; font-weight:600; vertical-align:super;\">YOUTUBE DOWNLOADER</span></p><p align=\"center\"><br/></p></body></html>"))
        self.label.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:22pt; font-weight:600;\">YOUTUBE DOWNLOADER</span></p></body></html>"))
        self.label_2.setText(_translate("Dialog", "LINK:"))
        self.audio.setText(_translate("Dialog", "ONLY AUDIO"))
        self.video.setText(_translate("Dialog", "VIDEO"))
        self.submit.setText(_translate("Dialog", "SUBMIT"))
        self.exit.setText(_translate("Dialog", "EXIT"))
        self.groupBox.setTitle(_translate("Dialog", "Download Status:"))
        self.TITLE.setText(_translate("Dialog", "NO DOWNLOADS"))

    def progress(self,stream,chunk,bytes_remaining):
        # pylint: disable=W0613
        filesize = stream.filesize
        bytes_received = filesize - bytes_remaining
        percent = round(100.0 * bytes_received / float(filesize), 1)
        self.progressBar.setProperty("value",percent)


    def video_down(self):
        url=self.LinkBox.text()
        self.typeName=""
        path=os.getcwd()
        if self.audio.isChecked():
            self.typeName=251
        if self.video.isChecked():
            self.typeName=18
        download=threading.Thread(target=self.download_thread,args=(url,self.typeName))
        download.start()

    def download_thread(self,url,types):
        _translate=QtCore.QCoreApplication.translate
        yt = YouTube(
        url,
        on_progress_callback=self.progress,
        on_complete_callback=None,
        proxies=None,
        use_oauth=False,
        allow_oauth_cache=True
    )
        self.TITLE.setText(_translate("Dialog",yt.title))
        self.groupBox.setTitle(_translate("Dialog", "Downloading...."))
        stream=yt.streams.get_by_itag(types)
        stream.download()
        self.groupBox.setTitle(_translate("Dialog", "Download completed:"))
        self.progressBar.setProperty("Dialog",0)
        
           
        
        
    def closeEvent(self, event):
        sys.exit(app.exec_())
        

if __name__ == "__main__":
    import sys


    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
