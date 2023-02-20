from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QFileDialog, QMessageBox, QDialog, QPushButton, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QMainWindow, QDialogButtonBox
from PyQt5.QtGui import QPixmap, QImage, QFont
from PIL import Image, ImageQt, ImageOps, ImageEnhance, ImageFilter, UnidentifiedImageError
from PIL.ImageQt import ImageQt
from pathlib import Path
import os
import cv2
import numpy as np
import sys
import randomizer


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(587, 617)
        self.buttonOkOrCancel = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonOkOrCancel.setGeometry(QtCore.QRect(220, 560, 341, 32))
        self.buttonOkOrCancel.setOrientation(QtCore.Qt.Horizontal)
        self.buttonOkOrCancel.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonOkOrCancel.setObjectName("buttonOkOrCancel")
        self.randomizerTitleLabel = QtWidgets.QLabel(Dialog)
        self.randomizerTitleLabel.setGeometry(QtCore.QRect(0, 0, 581, 61))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.randomizerTitleLabel.setFont(font)
        self.randomizerTitleLabel.setScaledContents(False)
        self.randomizerTitleLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.randomizerTitleLabel.setObjectName("randomizerTitleLabel")
        self.saturateBegin = QtWidgets.QLineEdit(Dialog)
        self.saturateBegin.setGeometry(QtCore.QRect(450, 380, 21, 20))
        self.saturateBegin.setObjectName("saturateBegin")
        self.rotateExplainer = QtWidgets.QLabel(Dialog)
        self.rotateExplainer.setGeometry(QtCore.QRect(60, 420, 331, 16))
        self.rotateExplainer.setObjectName("rotateExplainer")
        self.blurExplainer = QtWidgets.QLabel(Dialog)
        self.blurExplainer.setGeometry(QtCore.QRect(60, 500, 331, 16))
        self.blurExplainer.setObjectName("blurExplainer")
        self.saturateEnd = QtWidgets.QLineEdit(Dialog)
        self.saturateEnd.setGeometry(QtCore.QRect(490, 380, 21, 20))
        self.saturateEnd.setObjectName("saturateEnd")
        self.contrastBegin = QtWidgets.QLineEdit(Dialog)
        self.contrastBegin.setGeometry(QtCore.QRect(450, 300, 21, 20))
        self.contrastBegin.setObjectName("contrastBegin")
        self.sharpnessExplainer = QtWidgets.QLabel(Dialog)
        self.sharpnessExplainer.setGeometry(QtCore.QRect(60, 340, 331, 16))
        self.sharpnessExplainer.setObjectName("sharpnessExplainer")
        self.allowHorizontalFlip = QtWidgets.QCheckBox(Dialog)
        self.allowHorizontalFlip.setGeometry(QtCore.QRect(60, 160, 101, 17))
        self.allowHorizontalFlip.setObjectName("allowHorizontalFlip")
        self.blurEnd = QtWidgets.QLineEdit(Dialog)
        self.blurEnd.setGeometry(QtCore.QRect(490, 500, 21, 20))
        self.blurEnd.setObjectName("blurEnd")
        self.brightnessEnd = QtWidgets.QLineEdit(Dialog)
        self.brightnessEnd.setGeometry(QtCore.QRect(490, 260, 21, 20))
        self.brightnessEnd.setObjectName("brightnessEnd")
        self.allowGreyscale = QtWidgets.QCheckBox(Dialog)
        self.allowGreyscale.setGeometry(QtCore.QRect(60, 190, 101, 17))
        self.allowGreyscale.setObjectName("allowGreyscale")
        self.saturateExplainer = QtWidgets.QLabel(Dialog)
        self.saturateExplainer.setGeometry(QtCore.QRect(60, 380, 331, 16))
        self.saturateExplainer.setObjectName("saturateExplainer")
        self.brightnessBegin = QtWidgets.QLineEdit(Dialog)
        self.brightnessBegin.setGeometry(QtCore.QRect(450, 260, 21, 20))
        self.brightnessBegin.setObjectName("brightnessBegin")
        self.pixelateExplainer = QtWidgets.QLabel(Dialog)
        self.pixelateExplainer.setGeometry(QtCore.QRect(60, 460, 331, 16))
        self.pixelateExplainer.setObjectName("pixelateExplainer")
        self.rotateEnd = QtWidgets.QLineEdit(Dialog)
        self.rotateEnd.setGeometry(QtCore.QRect(490, 420, 21, 20))
        self.rotateEnd.setObjectName("rotateEnd")
        self.contrastExplainer = QtWidgets.QLabel(Dialog)
        self.contrastExplainer.setGeometry(QtCore.QRect(60, 300, 331, 16))
        self.contrastExplainer.setObjectName("contrastExplainer")
        self.sharpnessBegin = QtWidgets.QLineEdit(Dialog)
        self.sharpnessBegin.setGeometry(QtCore.QRect(450, 340, 21, 20))
        self.sharpnessBegin.setObjectName("sharpnessBegin")
        self.rotateBegin = QtWidgets.QLineEdit(Dialog)
        self.rotateBegin.setGeometry(QtCore.QRect(450, 420, 21, 20))
        self.rotateBegin.setObjectName("rotateBegin")
        self.brightnessExplainer = QtWidgets.QLabel(Dialog)
        self.brightnessExplainer.setGeometry(QtCore.QRect(60, 260, 331, 16))
        self.brightnessExplainer.setObjectName("brightnessExplainer")
        self.pixelateBegin = QtWidgets.QLineEdit(Dialog)
        self.pixelateBegin.setGeometry(QtCore.QRect(450, 460, 21, 20))
        self.pixelateBegin.setObjectName("pixelateBegin")
        self.sharpnessEnd = QtWidgets.QLineEdit(Dialog)
        self.sharpnessEnd.setGeometry(QtCore.QRect(490, 340, 21, 20))
        self.sharpnessEnd.setObjectName("sharpnessEnd")
        self.pixelateEnd = QtWidgets.QLineEdit(Dialog)
        self.pixelateEnd.setGeometry(QtCore.QRect(490, 460, 21, 20))
        self.pixelateEnd.setObjectName("pixelateEnd")
        self.allowVerticalFlip = QtWidgets.QCheckBox(Dialog)
        self.allowVerticalFlip.setGeometry(QtCore.QRect(60, 130, 101, 17))
        self.allowVerticalFlip.setObjectName("allowVerticalFlip")
        self.blurBegin = QtWidgets.QLineEdit(Dialog)
        self.blurBegin.setGeometry(QtCore.QRect(450, 500, 21, 20))
        self.blurBegin.setObjectName("blurBegin")
        self.allowRotate90 = QtWidgets.QCheckBox(Dialog)
        self.allowRotate90.setGeometry(QtCore.QRect(60, 100, 101, 17))
        self.allowRotate90.setObjectName("allowRotate90")
        self.contrastEnd = QtWidgets.QLineEdit(Dialog)
        self.contrastEnd.setGeometry(QtCore.QRect(490, 300, 21, 20))
        self.contrastEnd.setObjectName("contrastEnd")
        self.numOfPhotoLabel = QtWidgets.QLabel(Dialog)
        self.numOfPhotoLabel.setGeometry(QtCore.QRect(50, 550, 171, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.numOfPhotoLabel.setFont(font)
        self.numOfPhotoLabel.setObjectName("numOfPhotoLabel")
        self.numOfPhotoInput = QtWidgets.QLineEdit(Dialog)
        self.numOfPhotoInput.setGeometry(QtCore.QRect(220, 550, 61, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.numOfPhotoInput.setFont(font)
        self.numOfPhotoInput.setObjectName("numOfPhotoInput")
        self.warningLabel = QtWidgets.QLabel(Dialog)
        self.warningLabel.setGeometry(QtCore.QRect(220, 100, 311, 101))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.warningLabel.setFont(font)
        self.warningLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.warningLabel.setObjectName("warningLabel")

        self.retranslateUi(Dialog)
        self.buttonOkOrCancel.accepted.connect(Dialog.accept) # type: ignore
        self.buttonOkOrCancel.rejected.connect(Dialog.reject) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.randomizerTitleLabel.setText(_translate("Dialog", "Randomizer"))
        self.saturateBegin.setText(_translate("Dialog", "0"))
        self.rotateExplainer.setText(_translate("Dialog", "Rotate Scale: Default Scale = 90, Minimum = 0, Maximum = 180"))
        self.blurExplainer.setText(_translate("Dialog", "Blur Scale: Default Scale = 0, Minimum = 0, Maximum = 20"))
        self.saturateEnd.setText(_translate("Dialog", "20"))
        self.contrastBegin.setText(_translate("Dialog", "0"))
        self.sharpnessExplainer.setText(_translate("Dialog", "Sharpness Scale: Default Scale = 0, Minimum = 0, Maximum = 50"))
        self.allowHorizontalFlip.setText(_translate("Dialog", "Horizontal Flip?"))
        self.blurEnd.setText(_translate("Dialog", "20"))
        self.brightnessEnd.setText(_translate("Dialog", "20"))
        self.allowGreyscale.setText(_translate("Dialog", "Greyscale?"))
        self.saturateExplainer.setText(_translate("Dialog", "Saturate Scale: Default Scale = 10, Minimum = 0, Maximum = 20"))
        self.brightnessBegin.setText(_translate("Dialog", "0"))
        self.pixelateExplainer.setText(_translate("Dialog", "Pixelate Scale: Default Scale = 1, Minimum = 1, Maximum = 100"))
        self.rotateEnd.setText(_translate("Dialog", "180"))
        self.contrastExplainer.setText(_translate("Dialog", "Contrast Scale: Default Scale = 10, Minimum = 0, Maximum = 20"))
        self.sharpnessBegin.setText(_translate("Dialog", "0"))
        self.rotateBegin.setText(_translate("Dialog", "0"))
        self.brightnessExplainer.setText(_translate("Dialog", "Brightness Scale: Default Scale = 10, Minimum = 0, Maximum = 20"))
        self.pixelateBegin.setText(_translate("Dialog", "0"))
        self.sharpnessEnd.setText(_translate("Dialog", "50"))
        self.pixelateEnd.setText(_translate("Dialog", "100"))
        self.allowVerticalFlip.setText(_translate("Dialog", "Vertical Flip?"))
        self.blurBegin.setText(_translate("Dialog", "0"))
        self.allowRotate90.setText(_translate("Dialog", "Rotate 90?"))
        self.contrastEnd.setText(_translate("Dialog", "20"))
        self.numOfPhotoLabel.setText(_translate("Dialog", "Number of Photos:"))
        self.warningLabel.setText(_translate("Dialog", "Warning and Errors appear here."))

        self.buttonOkOrCancel.clicked.connect(self.handleButton)

    def handleButton(self, button):
        if button == self.buttonOkOrCancel.button(QDialogButtonBox.Ok):
            print("OK button was clicked")
        elif button == self.buttonOkOrCancel.button(QDialogButtonBox.Cancel):
            print("Cancel button was clicked")
            return




class Ui_MainWindow(object):
    def setupUi(self, MainWindow):

        # Image History Variables
        self.imageExists = False
        self.originalImage = None
        self.lowResImage = None
        self.pointer = -1
        self.steps = []
        self.dontRunFirstTime = False
        self.SecondWindow = None

        # Image change trackers
        self.listRotate90 = [0]
        self.listVerticalFlip = [False]
        self.listHorizontalFlip = [False]
        self.listGreyscale = [False]
        self.listBrightness = [1]
        self.listContrast = [1]
        self.listSharpness = [0]
        self.listSaturate = [1]
        self.listRotate = [90]
        self.listPixelate = [1]
        self.listBlur = [0]

        self.previousBrightness = 1
        self.previousContrast = 1
        self.previousSharpness = 0
        self.previousSaturate = 1
        self.previousRotate = 90
        self.previousPixelate = 1
        self.previousBlur = 0

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1080, 810)
        MainWindow.setMouseTracking(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.PhotoLabel = QtWidgets.QLabel(self.centralwidget)
        self.PhotoLabel.setGeometry(QtCore.QRect(-1, -1, 1081, 531))
        self.PhotoLabel.setText("")
        self.PhotoLabel.setObjectName("PhotoLabel")
        self.PhotoLabel.setScaledContents(True)

        # Original self.PhotoLabel
        self.originalPhotoLabelWidth = self.PhotoLabel.width()
        self.originalPhotoLabelHeight = self.PhotoLabel.height()

        self.WarningLabel = QtWidgets.QLabel(self.centralwidget)
        self.WarningLabel.setGeometry(QtCore.QRect(820, 570, 231, 161))
        self.WarningLabel.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.WarningLabel.setFont(QFont('Arial', 12))
        self.WarningLabel.setWordWrap(True)
        self.WarningLabel.setObjectName("WarningLabel")
        self.SaturationLabel = QtWidgets.QLabel(self.centralwidget)
        self.SaturationLabel.setGeometry(QtCore.QRect(210, 720, 71, 16))
        self.SaturationLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.SaturationLabel.setObjectName("SaturationLabel")
        self.BrightnessLabel = QtWidgets.QLabel(self.centralwidget)
        self.BrightnessLabel.setGeometry(QtCore.QRect(0, 720, 71, 16))
        self.BrightnessLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.BrightnessLabel.setObjectName("BrightnessLabel")
        self.ContrastLabel = QtWidgets.QLabel(self.centralwidget)
        self.ContrastLabel.setGeometry(QtCore.QRect(290, 720, 51, 16))
        self.ContrastLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.ContrastLabel.setObjectName("ContrastLabel")
        self.SharpenLabel = QtWidgets.QLabel(self.centralwidget)
        self.SharpenLabel.setGeometry(QtCore.QRect(80, 720, 51, 16))
        self.SharpenLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.SharpenLabel.setObjectName("SharpenLabel")
        self.BlurLabel = QtWidgets.QLabel(self.centralwidget)
        self.BlurLabel.setGeometry(QtCore.QRect(360, 720, 51, 16))
        self.BlurLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.BlurLabel.setObjectName("BlurLabel")
        self.PixelLabel = QtWidgets.QLabel(self.centralwidget)
        self.PixelLabel.setGeometry(QtCore.QRect(150, 720, 51, 16))
        self.PixelLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.PixelLabel.setObjectName("PixelLabel")
        self.HorizontalFlipButton = QtWidgets.QPushButton(self.centralwidget)
        self.HorizontalFlipButton.setGeometry(QtCore.QRect(530, 580, 121, 61))
        self.HorizontalFlipButton.setObjectName("HorizontalFlipButton")
        self.VerticalFlipButton = QtWidgets.QPushButton(self.centralwidget)
        self.VerticalFlipButton.setGeometry(QtCore.QRect(530, 660, 121, 61))
        self.VerticalFlipButton.setObjectName("VerticalFlipButton")
        self.RotateButton = QtWidgets.QPushButton(self.centralwidget)
        self.RotateButton.setGeometry(QtCore.QRect(670, 580, 121, 61))
        self.RotateButton.setObjectName("RotateButton")
        self.GrayScaleButton = QtWidgets.QPushButton(self.centralwidget)
        self.GrayScaleButton.setGeometry(QtCore.QRect(670, 660, 121, 61))
        self.GrayScaleButton.setObjectName("GrayScaleButton")
        self.RotateLabel = QtWidgets.QLabel(self.centralwidget)
        self.RotateLabel.setGeometry(QtCore.QRect(430, 720, 51, 16))
        self.RotateLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.RotateLabel.setObjectName("RotateLabel")
        self.BrightnessSlider = QtWidgets.QSlider(self.centralwidget)
        self.BrightnessSlider.setGeometry(QtCore.QRect(30, 560, 16, 160))
        self.BrightnessSlider.setMaximum(20)
        self.BrightnessSlider.setSliderPosition(10)
        self.BrightnessSlider.setPageStep(0)
        self.BrightnessSlider.setOrientation(QtCore.Qt.Vertical)
        self.BrightnessSlider.setObjectName("BrightnessSlider")
        self.SharpnessSlider = QtWidgets.QSlider(self.centralwidget)
        self.SharpnessSlider.setGeometry(QtCore.QRect(100, 560, 16, 160))
        self.SharpnessSlider.setMaximum(50)
        self.SharpnessSlider.setSliderPosition(0)
        self.SharpnessSlider.setPageStep(0)
        self.SharpnessSlider.setOrientation(QtCore.Qt.Vertical)
        self.SharpnessSlider.setObjectName("SharpnessSlider")
        self.PixelateSlider = QtWidgets.QSlider(self.centralwidget)
        self.PixelateSlider.setGeometry(QtCore.QRect(170, 560, 16, 160))
        self.PixelateSlider.setMinimum(1)
        self.PixelateSlider.setMaximum(100)
        self.PixelateSlider.setOrientation(QtCore.Qt.Vertical)
        self.PixelateSlider.setInvertedControls(True)
        self.PixelateSlider.setPageStep(0)
        self.PixelateSlider.setObjectName("PixelateSlider")
        self.SaturationSlider = QtWidgets.QSlider(self.centralwidget)
        self.SaturationSlider.setGeometry(QtCore.QRect(240, 560, 16, 160))
        self.SaturationSlider.setMaximum(20)
        self.SaturationSlider.setSliderPosition(10)
        self.SaturationSlider.setPageStep(0)
        self.SaturationSlider.setOrientation(QtCore.Qt.Vertical)
        self.SaturationSlider.setObjectName("SaturationSlider")
        self.ContrastSlider = QtWidgets.QSlider(self.centralwidget)
        self.ContrastSlider.setGeometry(QtCore.QRect(310, 560, 16, 160))
        self.ContrastSlider.setMaximum(20)
        self.ContrastSlider.setSliderPosition(10)
        self.ContrastSlider.setPageStep(0)
        self.ContrastSlider.setOrientation(QtCore.Qt.Vertical)
        self.ContrastSlider.setObjectName("ContrastSlider")
        self.BlurSlider = QtWidgets.QSlider(self.centralwidget)
        self.BlurSlider.setGeometry(QtCore.QRect(380, 560, 16, 160))
        self.BlurSlider.setMaximum(20)
        self.BlurSlider.setOrientation(QtCore.Qt.Vertical)
        self.BlurSlider.setPageStep(0)
        self.BlurSlider.setObjectName("BlurSlider")
        self.RotateSlider = QtWidgets.QSlider(self.centralwidget)
        self.RotateSlider.setGeometry(QtCore.QRect(450, 560, 16, 160))
        self.RotateSlider.setMaximum(180)
        self.RotateSlider.setSliderPosition(90)
        self.RotateSlider.setPageStep(0)
        self.RotateSlider.setOrientation(QtCore.Qt.Vertical)
        self.RotateSlider.setObjectName("RotateSlider")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1080, 26))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuEdit = QtWidgets.QMenu(self.menubar)
        self.menuEdit.setObjectName("menuEdit")
        self.menuRandomize = QtWidgets.QMenu(self.menubar)
        self.menuRandomize.setObjectName("menuRandomize")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionUpload = QtWidgets.QAction(MainWindow)
        self.actionUpload.setWhatsThis("")
        self.actionUpload.setObjectName("actionUpload")
        self.actionExport = QtWidgets.QAction(MainWindow)
        self.actionExport.setObjectName("actionExport")
        self.actionUndo = QtWidgets.QAction(MainWindow)
        self.actionUndo.setObjectName("actionUndo")
        self.actionRedo = QtWidgets.QAction(MainWindow)
        self.actionRedo.setWhatsThis("")
        self.actionRedo.setObjectName("actionRedo")
        self.actionRandomizer = QtWidgets.QAction(MainWindow)
        self.actionRandomizer.setVisible(True)
        self.actionRandomizer.setObjectName("actionRandomizer")
        self.menuFile.addAction(self.actionUpload)
        self.menuFile.addAction(self.actionExport)
        self.menuEdit.addAction(self.actionUndo)
        self.menuEdit.addAction(self.actionRedo)
        self.menuRandomize.addAction(self.actionRandomizer)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuRandomize.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.WarningLabel.setText(_translate("MainWindow", "Warnings/Errors Appear Here:"))
        self.SaturationLabel.setText(_translate("MainWindow", "Saturation"))
        self.BrightnessLabel.setText(_translate("MainWindow", "Brightness"))
        self.ContrastLabel.setText(_translate("MainWindow", "Contrast"))
        self.SharpenLabel.setText(_translate("MainWindow", "Sharpen"))
        self.BlurLabel.setText(_translate("MainWindow", "Blur"))
        self.PixelLabel.setText(_translate("MainWindow", "Pixelate"))
        self.HorizontalFlipButton.setText(_translate("MainWindow", "Horizontal Flip"))
        self.VerticalFlipButton.setText(_translate("MainWindow", "Vertical Flip"))
        self.RotateButton.setText(_translate("MainWindow", "Rotate (90°)"))
        self.GrayScaleButton.setText(_translate("MainWindow", "GrayScale"))
        self.RotateLabel.setText(_translate("MainWindow", "Rotate"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuEdit.setTitle(_translate("MainWindow", "Edit"))
        self.menuRandomize.setTitle(_translate("MainWindow", "Randomize"))
        self.actionUpload.setText(_translate("MainWindow", "Upload"))
        self.actionUpload.setToolTip(_translate("MainWindow", "Upload"))
        self.actionUpload.setStatusTip(_translate("MainWindow", "Upload files from device"))
        self.actionUpload.setShortcut(_translate("MainWindow", "Ctrl+U"))
        self.actionExport.setText(_translate("MainWindow", "Export"))
        self.actionExport.setStatusTip(_translate("MainWindow", "Saves image to existing file (assuming it exists)"))
        self.actionExport.setShortcut(_translate("MainWindow", "Ctrl+E"))
        self.actionUndo.setText(_translate("MainWindow", "Undo"))
        self.actionUndo.setStatusTip(_translate("MainWindow", "Undos previous action"))
        self.actionUndo.setShortcut(_translate("MainWindow", "Ctrl+Z"))
        self.actionRedo.setText(_translate("MainWindow", "Redo"))
        self.actionRedo.setStatusTip(_translate("MainWindow", "Redos last action"))
        self.actionRedo.setShortcut(_translate("MainWindow", "Ctrl+Shift+Z"))
        self.actionRandomizer.setText(_translate("MainWindow", "Randomizer"))
        self.actionRandomizer.setStatusTip(_translate("MainWindow", "Slightly randomizes current photo. More accurately resembles realistic training data."))
        self.actionRandomizer.setShortcut(_translate("MainWindow", "Ctrl+R"))

        # All actions:
        self.actionUpload.triggered.connect(self.importImage)
        self.actionUndo.triggered.connect(self.undo)
        self.actionRedo.triggered.connect(self.redo)
        self.actionExport.triggered.connect(self.export)
        self.actionRandomizer.triggered.connect(self.randomizer)

        self.RotateButton.clicked.connect(lambda: self.addStep('rotate 90'))
        self.VerticalFlipButton.clicked.connect(lambda: self.addStep('vertical flip'))
        self.HorizontalFlipButton.clicked.connect(lambda: self.addStep('horizontal flip'))
        self.GrayScaleButton.clicked.connect(lambda: self.addStep('greyscale'))
        
        self.BrightnessSlider.valueChanged.connect(self.brightness)  # change only last value
        self.BrightnessSlider.sliderReleased.connect(lambda: self.addStep('brightness'))
        self.ContrastSlider.valueChanged.connect(self.contrast)
        self.ContrastSlider.sliderReleased.connect(lambda: self.addStep('contrast'))
        self.SharpnessSlider.valueChanged.connect(self.sharpen)
        self.SharpnessSlider.sliderReleased.connect(lambda: self.addStep('sharpness'))
        self.SaturationSlider.valueChanged.connect(self.saturate)
        self.SaturationSlider.sliderReleased.connect(lambda: self.addStep('saturate'))
        self.BlurSlider.valueChanged.connect(self.blur)
        self.BlurSlider.sliderReleased.connect(lambda: self.addStep('blur'))
        self.RotateSlider.valueChanged.connect(self.rotate)
        self.RotateSlider.sliderReleased.connect(lambda: self.addStep('rotate'))
        self.PixelateSlider.valueChanged.connect(self.pixelate)
        self.PixelateSlider.sliderReleased.connect(lambda: self.addStep('pixelate'))

    def importImage(self):
        
        file_name, _ = QFileDialog.getOpenFileName() 
        try:
            self.originalImage = Image.open(file_name)
        except UnidentifiedImageError:
            file_extension = os.path.splitext(file_name)[-1]
            self.WarningLabel.setText(QtCore.QCoreApplication.translate("MainWindow", "Incorrect image file type"))
            msg_box = QMessageBox()

            msg_box.setText(f'{file_extension} files are not supported. Common supported files include: .jpg, .png, and .jpeg.')
            msg_box.setIcon(QMessageBox.Information)

            msg_box.addButton(QMessageBox.Ok)
            msg_box.exec_()

            return
        except:
            return
        width, height = self.originalImage.size

        new_scale_x = self.originalPhotoLabelWidth / width
        new_scale_y = self.originalPhotoLabelHeight / height

        if new_scale_x > new_scale_y:
            self.lowResImage = self.originalImage.resize((int(new_scale_x * width), int(new_scale_x * height)))
        else:
            self.lowResImage = self.originalImage.resize((int(new_scale_y * width), int(new_scale_y * height)))

        # Default values for new images
        if self.dontRunFirstTime:
            self.listRotate90.append(0)
            self.listVerticalFlip.append(False)
            self.listHorizontalFlip.append(False)
            self.listGreyscale.append(False)

            self.listBrightness.append(1)
            self.listContrast.append(1)
            self.listSharpness.append(0)
            self.listSaturate.append(1)
            self.listRotate.append(90)
            self.listPixelate.append(1)
            self.listBlur.append(0)
        else:
            self.dontRunFirstTime = True

        self.imageExists = True

        self.pointer += 1
        self.defaultSliderPosition()
        self.reconstructImage()
            
    # make random function next
    
    def export(self):
        if not self.imageExists:
            self.WarningLabel.setText(QtCore.QCoreApplication.translate("MainWindow", "NOTHING TO EXPORT"))
            return

        folderpath, _ = QtWidgets.QFileDialog.getSaveFileName(caption="Export File", filter="Images (*.png)") 
        final_image = self.originalResolutionReconstructImage()

        try:
            final_image = final_image.save(folderpath)
        except:
            return
        
        self.WarningLabel.setText(QtCore.QCoreApplication.translate("MainWindow", "EXPORTED SUCCESSFULLY"))

    def originalResolutionReconstructImage(self):
        new_image = self.originalImage.rotate(90 * self.listRotate90[self.pointer], Image.Resampling.NEAREST, expand = 1)

        if self.listVerticalFlip[self.pointer]:
            new_image = new_image.transpose(Image.Transpose.FLIP_TOP_BOTTOM)

        if self.listHorizontalFlip[self.pointer]:
            new_image = new_image.transpose(Image.Transpose.FLIP_LEFT_RIGHT)

        if self.listGreyscale[self.pointer]:
            new_image = ImageOps.grayscale(new_image)

        if not self.listBrightness[self.pointer] == 1:
            new_image = ImageEnhance.Brightness(new_image)
            new_image = new_image.enhance(self.listBrightness[self.pointer])

        if not self.listContrast[self.pointer] == 1:
            new_image = ImageEnhance.Contrast(new_image)
            new_image = new_image.enhance(self.listContrast[self.pointer])

        if not self.listSharpness[self.pointer] == 0:
            new_image = ImageEnhance.Sharpness(new_image)
            new_image = new_image.enhance(self.listSharpness[self.pointer])

        if not self.listSaturate[self.pointer] == 1:
            new_image = ImageEnhance.Color(new_image)
            new_image = new_image.enhance(self.listSaturate[self.pointer])

        if not self.listBlur[self.pointer] == 0:
            new_image = new_image.filter(ImageFilter.GaussianBlur(radius = self.listBlur[-1]))

        new_image = new_image.rotate(self.listRotate[self.pointer] - 90, Image.Resampling.NEAREST, expand = 1)

        if not self.listPixelate[self.pointer] == 1:
            original_size = new_image.size
            small_image = new_image.resize((int(original_size[0] / self.listPixelate[self.pointer]), int(original_size[1] / self.listPixelate[self.pointer])), Image.Resampling.BILINEAR)
            new_image = small_image.resize(original_size, Image.Resampling.NEAREST)

        return new_image

    def brightness(self):
        if not self.imageExists:
            self.WarningLabel.setText(QtCore.QCoreApplication.translate("MainWindow", "UPLOAD AN IMAGE"))
            return

        self.destroyRedo()
        self.listBrightness[-1] = self.BrightnessSlider.value() / 10
        self.reconstructImage()

    def contrast(self):
        if not self.imageExists:
            self.WarningLabel.setText(QtCore.QCoreApplication.translate("MainWindow", "UPLOAD AN IMAGE"))
            return

        self.destroyRedo()
        self.listContrast[-1] = self.ContrastSlider.value() / 10
        self.reconstructImage()

    def sharpen(self):
        if not self.imageExists:
            self.WarningLabel.setText(QtCore.QCoreApplication.translate("MainWindow", "UPLOAD AN IMAGE"))
            return

        self.destroyRedo()
        self.listSharpness[-1] = self.SharpnessSlider.value() / 10
        self.reconstructImage()

    def saturate(self):
        if not self.imageExists:
            self.WarningLabel.setText(QtCore.QCoreApplication.translate("MainWindow", "UPLOAD AN IMAGE"))
            return

        self.destroyRedo()
        self.listSaturate[-1] = self.SaturationSlider.value() / 10
        self.reconstructImage()

    def blur(self):
        if not self.imageExists:
            self.WarningLabel.setText(QtCore.QCoreApplication.translate("MainWindow", "UPLOAD AN IMAGE"))
            return

        self.destroyRedo()
        self.listBlur[-1] = self.BlurSlider.value()
        self.reconstructImage()

    def rotate(self):
        if not self.imageExists:
            self.WarningLabel.setText(QtCore.QCoreApplication.translate("MainWindow", "UPLOAD AN IMAGE"))
            return

        self.destroyRedo()
        self.listRotate[-1] = self.RotateSlider.value()
        self.reconstructImage()

    def pixelate(self):
        if not self.imageExists:
            self.WarningLabel.setText(QtCore.QCoreApplication.translate("MainWindow", "UPLOAD AN IMAGE"))
            return

        self.destroyRedo()
        self.listPixelate[-1] = self.PixelateSlider.value()
        self.reconstructImage()

    def addStep(self, instruction):

        if not self.imageExists:
            self.WarningLabel.setText(QtCore.QCoreApplication.translate("MainWindow", "UPLOAD AN IMAGE"))
            return

        self.destroyRedo()                

        # rotate 90
        if instruction == 'rotate 90':
            if self.listRotate90 == 4:
                self.listRotate90.append(0)
            else:
                self.listRotate90.append(self.listRotate90[-1] + 1)
        else:
            self.listRotate90.append(self.listRotate90[-1])

        # vertical flip
        if instruction == 'vertical flip':
            self.listVerticalFlip.append(not self.listVerticalFlip[-1])
        else:
            self.listVerticalFlip.append(self.listVerticalFlip[-1])

        # horizontal flip
        if instruction == 'horizontal flip':
            self.listHorizontalFlip.append(not self.listHorizontalFlip[-1])
        else:
            self.listHorizontalFlip.append(self.listHorizontalFlip[-1])
        
        # greyscale
        if instruction == 'greyscale':
            self.listGreyscale.append(True)
        else:
            self.listGreyscale.append(self.listGreyscale[-1])

        # brightness
        if instruction == 'brightness':
            self.listBrightness[-1] = self.previousBrightness
            self.listBrightness.append(self.BrightnessSlider.value() / 10)
            self.previousBrightness = self.listBrightness[-1]
        else:
            self.listBrightness.append(self.listBrightness[-1])

        # contrast
        if instruction == 'contrast':
            self.listContrast[-1] = self.previousContrast
            self.listContrast.append(self.ContrastSlider.value() / 10)
            self.previousContrast = self.listContrast[-1]
        else:
            self.listContrast.append(self.listContrast[-1])

        # sharpen
        if instruction == 'sharpness':
            self.listSharpness[-1] = self.previousSharpness
            self.listSharpness.append(self.SharpnessSlider.value() / 10)
            self.previousSharpness = self.listSharpness[-1]
        else:
            self.listSharpness.append(self.listSharpness[-1])

        # saturate
        if instruction == 'saturate':
            self.listSaturate[-1] = self.previousSaturate
            self.listSaturate.append(self.SaturationSlider.value() / 10)
            self.previousSaturate = self.listSaturate[-1]
        else:
            self.listSaturate.append(self.listSaturate[-1])

        # blur
        if instruction == 'blur':
            self.listBlur[-1] = self.previousBlur
            self.listBlur.append(self.BlurSlider.value())
            self.previousBlur = self.listBlur[-1]
        else:
            self.listBlur.append(self.listBlur[-1])

        # rotate
        if instruction == 'rotate':
            self.listRotate[-1] = self.previousRotate
            self.listRotate.append(self.RotateSlider.value())
            self.previousRotate = self.listRotate[-1]
        else:
            self.listRotate.append(self.listRotate[-1])

        # pixelate
        if instruction == 'pixelate':
            self.listPixelate[-1] = self.previousPixelate
            self.listPixelate.append(self.PixelateSlider.value())
            self.previousPixelate = self.listPixelate[-1]
        else:
            self.listPixelate.append(self.listPixelate[-1])

        self.pointer += 1
        self.reconstructImage()

    def reconstructImage(self):

        new_image = self.lowResImage.rotate(90 * self.listRotate90[self.pointer], Image.Resampling.NEAREST, expand = 1)

        if self.listVerticalFlip[self.pointer]:
            new_image = new_image.transpose(Image.Transpose.FLIP_TOP_BOTTOM)

        if self.listHorizontalFlip[self.pointer]:
            new_image = new_image.transpose(Image.Transpose.FLIP_LEFT_RIGHT)

        if self.listGreyscale[self.pointer]:
            new_image = ImageOps.grayscale(new_image)

        if not self.listBrightness[self.pointer] == 1:
            new_image = ImageEnhance.Brightness(new_image)
            new_image = new_image.enhance(self.listBrightness[self.pointer])

        if not self.listContrast[self.pointer] == 1:
            new_image = ImageEnhance.Contrast(new_image)
            new_image = new_image.enhance(self.listContrast[self.pointer])

        if not self.listSharpness[self.pointer] == 0:
            new_image = ImageEnhance.Sharpness(new_image)
            new_image = new_image.enhance(self.listSharpness[self.pointer])

        if not self.listSaturate[self.pointer] == 1:
            new_image = ImageEnhance.Color(new_image)
            new_image = new_image.enhance(self.listSaturate[self.pointer])

        if not self.listBlur[self.pointer] == 0:
            new_image = new_image.filter(ImageFilter.GaussianBlur(radius = self.listBlur[-1]))

        new_image = new_image.rotate(self.listRotate[self.pointer] - 90, Image.Resampling.NEAREST, expand = 1)

        if not self.listPixelate[self.pointer] == 1:
            original_size = new_image.size
            small_image = new_image.resize((int(original_size[0] / self.listPixelate[self.pointer]), int(original_size[1] / self.listPixelate[self.pointer])), Image.Resampling.BILINEAR)
            new_image = small_image.resize(original_size, Image.Resampling.NEAREST)

        self.PhotoLabel.setPixmap(self.PILtoPIX(new_image))

        self.resizePhotoLabel(new_image)

    def undo(self):
        
        try:
            if self.pointer > 0:
                self.pointer -= 1
                self.defaultSliderPosition()
                self.reconstructImage()
                self.WarningLabel.setText(QtCore.QCoreApplication.translate("MainWindow", "Undo successful"))
            else:
                self.WarningLabel.setText(QtCore.QCoreApplication.translate("MainWindow", "Can't undo further"))
        except:
            self.pointer += 1 # Keeps pointer in same position
            self.WarningLabel.setText(QtCore.QCoreApplication.translate("MainWindow", "Can't undo further"))

    def redo(self):
        try:
            self.pointer += 1
            self.defaultSliderPosition()
            self.reconstructImage()
            self.WarningLabel.setText(QtCore.QCoreApplication.translate("MainWindow", "Redo successful"))
        except:
            self.pointer -= 1 # Keeps point in same position
            self.WarningLabel.setText(QtCore.QCoreApplication.translate("MainWindow", "Can't redo further"))

    def destroyRedo(self):
        self.listRotate90 = self.listRotate90[:self.pointer + 1]
        self.listVerticalFlip = self.listVerticalFlip[:self.pointer + 1]
        self.listHorizontalFlip = self.listHorizontalFlip[:self.pointer + 1]
        self.listGreyscale = self.listGreyscale[:self.pointer + 1]
        self.listBrightness = self.listBrightness[:self.pointer + 1]
        self.listContrast = self.listContrast[:self.pointer + 1]
        self.listSharpness = self.listSharpness[:self.pointer + 1]
        self.listSaturate = self.listSaturate[:self.pointer + 1]
        self.listRotate = self.listRotate[:self.pointer + 1]
        self.listPixelate = self.listPixelate[:self.pointer + 1]
        self.listBlur = self.listBlur[:self.pointer + 1]

    def defaultSliderPosition(self):
        self.BrightnessSlider.setSliderPosition(int(self.listBrightness[self.pointer] * 10))
        self.SharpnessSlider.setSliderPosition(int(self.listSharpness[self.pointer] * 10))
        self.SaturationSlider.setSliderPosition(int(self.listSaturate[self.pointer] * 10))
        self.ContrastSlider.setSliderPosition(int(self.listContrast[self.pointer] * 10))
        self.RotateSlider.setSliderPosition(int(self.listRotate[self.pointer]))
        self.PixelateSlider.setSliderPosition(int(self.listPixelate[self.pointer]))
        self.BlurSlider.setSliderPosition(int(self.listBlur[self.pointer]))

    def randomizer(self):

        if not self.imageExists:
            self.WarningLabel.setText(QtCore.QCoreApplication.translate("MainWindow", "Please import an image first before trying to randomize"))
            return

        SecondaryWindow = QtWidgets.QDialog()
        dialog = Ui_Dialog()
        dialog.setupUi(SecondaryWindow)
        SecondaryWindow.show()
        if SecondaryWindow.exec_():
            print(":(")

    def resizePhotoLabel(self, im):
        width, height = im.size
        new_scale_x = self.originalPhotoLabelWidth / width
        new_scale_y = self.originalPhotoLabelHeight / height
        if new_scale_x < new_scale_y:
            self.PhotoLabel.setGeometry(int(self.originalPhotoLabelWidth / 2 - (width * new_scale_x / 2)), 0, int(width * new_scale_x), int(height * new_scale_x))
        else:
            self.PhotoLabel.setGeometry(int(self.originalPhotoLabelWidth / 2 - (width * new_scale_y / 2)), 0, int(width * new_scale_y), int(height * new_scale_y))

    def PILtoPIX(self, im):
        if im.mode == "RGB":
            r, g, b = im.split()
            im = Image.merge("RGB", (b, g, r))
        elif  im.mode == "RGBA":
            r, g, b, a = im.split()
            im = Image.merge("RGBA", (b, g, r, a))
        elif im.mode == "L":
            im = im.convert("RGBA")
        im2 = im.convert("RGBA")
        data = im2.tobytes("raw", "RGBA")
        qim = QtGui.QImage(data, im.size[0], im.size[1], QtGui.QImage.Format_ARGB32)
        pixmap = QtGui.QPixmap.fromImage(qim)
        return pixmap

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())