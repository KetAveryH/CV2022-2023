# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'buttonTest.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Photo = QtWidgets.QLabel(self.centralwidget)
        self.Photo.setGeometry(QtCore.QRect(0, 0, 801, 471))
        self.Photo.setText("")
        self.Photo.setPixmap(QtGui.QPixmap("blueangels-det.jpg"))
        self.Photo.setScaledContents(True)
        self.Photo.setObjectName("Photo")
        self.AirplaneButton = QtWidgets.QPushButton(self.centralwidget)
        self.AirplaneButton.setGeometry(QtCore.QRect(0, 470, 331, 61))
        self.AirplaneButton.setObjectName("AirplaneButton")
        self.IntersectionButton = QtWidgets.QPushButton(self.centralwidget)
        self.IntersectionButton.setGeometry(QtCore.QRect(450, 470, 351, 61))
        self.IntersectionButton.setObjectName("IntersectionButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.AirplaneButton.clicked.connect(self.show_plane)
        self.IntersectionButton.clicked.connect(self.show_car)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.AirplaneButton.setText(_translate("MainWindow", "Airplanes"))
        self.IntersectionButton.setText(_translate("MainWindow", "Car Intersection"))

    def show_plane(self):
        self.Photo.setPixmap(QtGui.QPixmap("blueangels-det.jpg"))
    def show_car(self):
        self.Photo.setPixmap(QtGui.QPixmap("Intersection-Counts-det.jpg"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
