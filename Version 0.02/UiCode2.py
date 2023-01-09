# -*- coding: utf-8 -*-

#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QFileDialog
from PIL import Image, ImageQt
import tempfile
import cv2
import numpy as np


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        #Reading necessary files
        buttonStyle = open("Styling/buttonStyling.txt", "r") 

        #Declaring some of my own variables
        self.numpyImage = None
        self.displayImage = None
        self.prevImage = None

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(0, 0, 161, 431))
        self.groupBox.setStyleSheet("QGroupBox {\n"
"    background-color: grey;\n"
"\n"
"    border: 2px solid black;\n"
"    border-radius: 10px\n"
"}")
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.widget = QtWidgets.QWidget(self.groupBox)
        self.widget.setGeometry(QtCore.QRect(20, 40, 120, 348))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(25)
        self.verticalLayout.setObjectName("verticalLayout")
        self.flipButton = QtWidgets.QPushButton(self.widget)
        self.flipButton.setStyleSheet(str(buttonStyle)) #Opens the styling string generated by Pyqt5, I just wrote it to a file to make the code more compact
        self.flipButton.setObjectName("flipButton")
        self.verticalLayout.addWidget(self.flipButton)
        self.randomZoomButton = QtWidgets.QPushButton(self.widget)
        self.randomZoomButton.setStyleSheet(str(buttonStyle))
        self.randomZoomButton.setObjectName("randomZoomButton")
        self.verticalLayout.addWidget(self.randomZoomButton)
        self.rgbChangeButton = QtWidgets.QPushButton(self.widget)
        self.rgbChangeButton.setStyleSheet(str(buttonStyle))
        self.rgbChangeButton.setObjectName("rgbChangeButton")
        self.verticalLayout.addWidget(self.rgbChangeButton)
        self.greyscaleButton = QtWidgets.QPushButton(self.widget)
        self.greyscaleButton.setStyleSheet(str(buttonStyle)) 
        self.greyscaleButton.setObjectName("greyscaleButton")
        self.verticalLayout.addWidget(self.greyscaleButton)
        self.rotateButton = QtWidgets.QPushButton(self.widget)
        self.rotateButton.setStyleSheet(str(buttonStyle)) 
        self.rotateButton.setObjectName("rotateButton")
        self.verticalLayout.addWidget(self.rotateButton)
        self.pushButton = QtWidgets.QPushButton(self.widget)
        self.pushButton.setSizeIncrement(QtCore.QSize(0, 0))
        self.pushButton.setStyleSheet(str(buttonStyle))
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(0, 440, 791, 111))
        self.groupBox_2.setStyleSheet("QGroupBox {\n"      #This is an example of how pyqt automatically keeps track of its styling.
"    background-color: grey;\n"
"\n"
"    border: 2px solid black;\n"
"}")
        self.groupBox_2.setTitle("")
        self.groupBox_2.setObjectName("groupBox_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(180, 10, 591, 411))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(self.displayImage)) # It seems like this only runs once at start up? 
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
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
        self.actionImport_File = QtWidgets.QAction(MainWindow)
        self.actionImport_File.setObjectName("actionImport_File")
        self.actionSave_Image = QtWidgets.QAction(MainWindow)
        self.actionSave_Image.setObjectName("actionSave_Image")
        self.menuFile.addAction(self.actionImport_File)
        self.menuFile.addAction(self.actionSave_Image)
        self.menubar.addAction(self.menuFile.menuAction())

        self.actionImport_File.triggered.connect(self.importImage)
        self.flipButton.clicked.connect(self.flipImage)
        self.randomZoomButton.clicked.connect(self.randomZoom)
        self.greyscaleButton.clicked.connect(self.greyscale)
        self.rotateButton.clicked.connect(self.rotate)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    #Button Functions

    def importImage(self):
        file_name, _ = QFileDialog.getOpenFileName()  #This will prompt the user with a file navigation box
        tempIm = Image.open(str(file_name))
        self.numpyImage = np.asarray(tempIm)
        # self.numpyImage = cv2.imread(str(file_name)) #Should work, but file formats conflict, BGR instead of RGB
        img = Image.fromarray(self.numpyImage, mode='RGB')  
        self.displayImage = ImageQt.ImageQt(img)
        self.label.setPixmap(QtGui.QPixmap.fromImage(self.displayImage)) #I included this since the "setPixmap" does not run automatically for some reason, but triggered does?

    def flipImage(self):
        
        self.numpyImage = cv2.flip(self.numpyImage, 0) 
        img = Image.fromarray(self.numpyImage, mode='RGB')
        self.displayImage = ImageQt.ImageQt(img)
        self.label.setPixmap(QtGui.QPixmap.fromImage(self.displayImage))

    def randomZoom(self): #For this we would usually have (self, cropheight, cropWidth), but we will set constant values for now since I don't know how to make pop_ups.
        """This function takes in a crop heigh and width, and cuts out a random portion of the given
         image and writes it to a file called randomZoomOut. DOESN'T WORK AFTER FIRST USE,
         
         TO DO: we would want to be able to run random zoom on a single image multiple times without 
         having to reload the image each time.
         """ 
        img = self.numpyImage
        crop_width = 64
        crop_height = 64

        max_x = img.shape[1] - crop_width
        max_y = img.shape[0] - crop_height

        x = np.random.randint(0, max_x)
        y = np.random.randint(0, max_y)

        self.numpyImage = img[y: y + crop_height, x: x + crop_width]
        img = Image.fromarray(self.numpyImage, mode='RGB')

        self.displayImage = ImageQt.ImageQt(img)   #Displays our saved Image
        self.label.setPixmap(QtGui.QPixmap.fromImage(self.displayImage))
        

    def greyscale(self):    # Will greyscale the shown image
        # img = cv2.imread(str(self.displayImage), 0)
        img = self.numpyImage
        
        img = Image.fromarray(self.numpyImage, mode='RGB')  #Displays
        self.numpyImage = cv2.cvtColor(self.numpyImage, cv2.COLOR_BGR2GRAY)  #Updates our file

        self.displayImage = ImageQt.ImageQt(img)   #Displays our saved Image
        self.label.setPixmap(QtGui.QPixmap.fromImage(self.displayImage))



    def rotate(self):       # Will rotate an image 90 degrees clockwise
        img = self.numpyImage
        img = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)
        img = Image.fromarray(self.numpyImage, mode='RGB')  #Displays
        
        self.displayImage = ImageQt.ImageQt(img)   #Displays our saved Image
        self.label.setPixmap(QtGui.QPixmap.fromImage(self.displayImage))


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.flipButton.setText(_translate("MainWindow", "Flip"))
        self.randomZoomButton.setText(_translate("MainWindow", "Random \n"
" Zoom"))
        self.rgbChangeButton.setText(_translate("MainWindow", "RGB Change"))
        self.greyscaleButton.setText(_translate("MainWindow", "Greyscale"))
        self.rotateButton.setText(_translate("MainWindow", "Rotate"))
        self.pushButton.setText(_translate("MainWindow", "PushButton"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.actionImport_File.setText(_translate("MainWindow", "Import File"))
        self.actionSave_Image.setText(_translate("MainWindow", "Save Image"))





if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
