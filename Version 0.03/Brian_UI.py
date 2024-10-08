# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Brian_UI.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QFileDialog, QMessageBox
from PyQt5.QtGui import QPixmap, QImage
from PIL import Image, ImageQt
import cv2
import numpy as np
import sys



class Ui_MainWindow(object):
    def setupUi(self, MainWindow):

        # Reading necessary files
        # buttonStyle = open(r"C:\Users\brian\Desktop\MuddSub\CV2022-2023\Version 0.01\Styling\buttonStyling.txt", "r") 

        # Ket Vars 
        self.numpyImage = None
        self.displayImage = None
        self.prevImage = None

        # other declarations (mine)
        self.cvImage = None
        self.QImage = None
        self.history = []

        self.pointer = -1
        self.cvHistory = []
        self.QHistory = []

        self.folderPath = None

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(20, 20, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(20, 60, 93, 28))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(20, 100, 93, 28))
        self.pushButton_3.setObjectName("pushButton_3")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(140, 20, 621, 431))
        self.label.setObjectName("label")
        self.label.setScaledContents(True)
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(20, 140, 93, 28))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(20, 180, 93, 28))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(20, 220, 93, 28))
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_7.setGeometry(QtCore.QRect(20, 260, 93, 28))
        self.pushButton_7.setObjectName("pushButton_7")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionUpload = QtWidgets.QAction(MainWindow)
        self.actionUpload.setObjectName("actionUpload")
        self.actionExport = QtWidgets.QAction(MainWindow)
        self.actionExport.setObjectName("actionExport")
        self.menuFile.addAction(self.actionUpload)
        self.menuFile.addAction(self.actionExport)
        self.menubar.addAction(self.menuFile.menuAction())


        
        

        self.actionUpload.triggered.connect(self.importImage)
        self.actionExport.triggered.connect(self.export)
        self.pushButton.clicked.connect(self.flipImage)
        self.pushButton_2.clicked.connect(self.randomZoom)
        self.pushButton_3.clicked.connect(self.RGB)
        self.pushButton_4.clicked.connect(self.greyscale)
        self.pushButton_5.clicked.connect(self.rotate)
        self.pushButton_6.clicked.connect(self.undo)
        self.pushButton_7.clicked.connect(self.redo)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Flip"))
        self.pushButton_2.setText(_translate("MainWindow", "Random Zoom"))
        self.pushButton_3.setText(_translate("MainWindow", "RGB Change"))
        self.label.setText(_translate("MainWindow", ""))
        self.pushButton_4.setText(_translate("MainWindow", "GrayScale"))
        self.pushButton_5.setText(_translate("MainWindow", "Rotate"))
        self.pushButton_6.setText(_translate("MainWindow", "Undo"))
        self.pushButton_7.setText(_translate("MainWindow", "Redo"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.actionUpload.setText(_translate("MainWindow", "Upload"))
        self.actionExport.setText(_translate("MainWindow", "Export"))



        


    def importImage(self):
        file_name, _ = QFileDialog.getOpenFileName()  #This will prompt the user with a file navigation box
        if file_name == "":
            return

        self.pointer += 1
        self.cvHistory.append(cv2.imread(file_name))
        self.QHistory.append(self.cvToQ(self.cvHistory[self.pointer]))
        self.label.setPixmap(QtGui.QPixmap.fromImage(self.QHistory[self.pointer]))



    def flipImage(self):
        self.destroyRedo()
        flipped_image = cv2.flip(self.cvHistory[self.pointer], 0)

        self.cvHistory.append(flipped_image)
        self.QHistory.append(self.cvToQ(flipped_image))

        self.pointer += 1
        self.label.setPixmap(QtGui.QPixmap.fromImage(self.QHistory[self.pointer]))

    def randomZoom(self):
        try:
            self.destroyRedo()
            max_height, max_width, _ = self.cvHistory[self.pointer].shape
            top_height = np.random.randint(0, max_height)
            top_width = np.random.randint(0, max_width)

            bottom_height = np.random.randint(0, max_height - top_height)
            bottom_width = np.random.randint(0, max_width - top_width)
            
            zoomed_image = self.cvHistory[self.pointer][bottom_height:top_height, bottom_width:top_width]
            self.cvHistory.append(zoomed_image)
            self.QHistory.append(self.cvToQ(zoomed_image))

            self.pointer += 1
            self.label.setPixmap(QtGui.QPixmap.fromImage(self.QHistory[self.pointer]))
        except:
            print("can't zoom anymore")

    def RGB(self):
        self.destroyRedo()
        BGR_image = cv2.cvtColor(self.cvHistory[self.pointer], cv2.COLOR_BGR2RGB)

        self.cvHistory.append(BGR_image)
        self.QHistory.append(self.cvToQ(BGR_image))

        self.pointer += 1
        self.label.setPixmap(QtGui.QPixmap.fromImage(self.QHistory[self.pointer]))


    def greyscale(self):
        self.destroyRedo()
        try:
            grey_image = cv2.cvtColor(self.cvHistory[self.pointer], cv2.COLOR_BGR2GRAY)

            self.cvHistory.append(grey_image)
            self.QHistory.append(self.cvToQ(grey_image))

            self.pointer += 1
            self.label.setPixmap(QtGui.QPixmap.fromImage(self.QHistory[self.pointer]))
        except:
            print("Can't grayscale (again)")

    def rotate(self):
        self.destroyRedo()
        try:
            rotate_iamge = cv2.rotate(self.cvHistory[self.pointer], cv2.ROTATE_90_CLOCKWISE)

            self.cvHistory.append(rotate_iamge)
            self.QHistory.append(self.cvToQ(rotate_iamge))

            self.pointer += 1
            self.label.setPixmap(QtGui.QPixmap.fromImage(self.QHistory[self.pointer]))
        except:
            print("Can't rotate")


    def undo(self):
        try:
            if self.pointer > 0:
                self.pointer -= 1
                self.label.setPixmap(QtGui.QPixmap.fromImage(self.QHistory[self.pointer]))
            else:
                print("Can't undo further")
        except:
            self.pointer += 1 # Keeps pointer in same position
            print("Can't undo further also")

    def redo(self):
        try:
            self.pointer += 1
            self.label.setPixmap(QtGui.QPixmap.fromImage(self.QHistory[self.pointer]))
        except:
            self.pointer -= 1 # Keeps point in same position
            print("Can't redo further")

    def destroyRedo(self):
        self.cvHistory = self.cvHistory[:self.pointer + 1]
        self.QHistory = self.QHistory[:self.pointer + 1]


    def cvToQ(self, cvImg):
        cvImg = cv2.cvtColor(cvImg, cv2.COLOR_BGR2RGB)
        height, width, channel = cvImg.shape
        bytesPerLine = 3 * width
        qImg = QImage(cvImg.data, width, height, bytesPerLine, QImage.Format_RGB888)
        return qImg

    def export(self):
        while True:
            try:
                folderpath, _ = QtWidgets.QFileDialog.getSaveFileName(caption="Export File", filter="Images (*.png *.jpg)") 
                cv2.imwrite(folderpath, self.cvHistory[self.pointer])
                break

            except: 
                if folderpath == "":          # Handles the cancel case 
                    print("No FilePath Selected")
                else:
                    print("Export Error")
                break




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
