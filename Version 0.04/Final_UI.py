# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Final_UI.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QFileDialog
from PyQt5.QtGui import QPixmap, QImage
from PIL import Image, ImageQt, ImageOps, ImageEnhance, ImageFilter
from PIL.ImageQt import ImageQt
import cv2
import numpy as np
import sys


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):

        # Image History Variables
        self.PILHistory = []
        self.instructionList = []
        self.pointer = -1

        # instruction values
        '''
        0. rotate ninety
        1. vertical flip
        2. horizontal flip
        3. greyscale
        4. brightness (scale)
        5. contrast (scale)
        6. sharpen (scale)
        7. saturate (scale)
        8. blur (scale)
        9. rotate (scale)
        10. pixelate (scale)
        '''

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
        self.BrightnessSlider.setOrientation(QtCore.Qt.Vertical)
        self.BrightnessSlider.setObjectName("BrightnessSlider")
        self.SharpnessSlider = QtWidgets.QSlider(self.centralwidget)
        self.SharpnessSlider.setGeometry(QtCore.QRect(100, 560, 16, 160))
        self.SharpnessSlider.setMaximum(50)
        self.SharpnessSlider.setSliderPosition(0)
        self.SharpnessSlider.setOrientation(QtCore.Qt.Vertical)
        self.SharpnessSlider.setObjectName("SharpnessSlider")
        self.PixelateSlider = QtWidgets.QSlider(self.centralwidget)
        self.PixelateSlider.setGeometry(QtCore.QRect(170, 560, 16, 160))
        self.PixelateSlider.setMinimum(1)
        self.PixelateSlider.setMaximum(100)
        self.PixelateSlider.setOrientation(QtCore.Qt.Vertical)
        self.PixelateSlider.setInvertedControls(True)
        self.PixelateSlider.setObjectName("PixelateSlider")
        self.SaturationSlider = QtWidgets.QSlider(self.centralwidget)
        self.SaturationSlider.setGeometry(QtCore.QRect(240, 560, 16, 160))
        self.SaturationSlider.setMaximum(20)
        self.SaturationSlider.setSliderPosition(10)
        self.SaturationSlider.setOrientation(QtCore.Qt.Vertical)
        self.SaturationSlider.setObjectName("SaturationSlider")
        self.ContrastSlider = QtWidgets.QSlider(self.centralwidget)
        self.ContrastSlider.setGeometry(QtCore.QRect(310, 560, 16, 160))
        self.ContrastSlider.setMaximum(20)
        self.ContrastSlider.setSliderPosition(10)
        self.ContrastSlider.setOrientation(QtCore.Qt.Vertical)
        self.ContrastSlider.setObjectName("ContrastSlider")
        self.BlurSlider = QtWidgets.QSlider(self.centralwidget)
        self.BlurSlider.setGeometry(QtCore.QRect(380, 560, 16, 160))
        self.BlurSlider.setMaximum(20)
        self.BlurSlider.setOrientation(QtCore.Qt.Vertical)
        self.BlurSlider.setObjectName("BlurSlider")
        self.RotateSlider = QtWidgets.QSlider(self.centralwidget)
        self.RotateSlider.setGeometry(QtCore.QRect(450, 560, 16, 160))
        self.RotateSlider.setMaximum(180)
        self.RotateSlider.setSliderPosition(90)
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
        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")
        self.actionSave_As = QtWidgets.QAction(MainWindow)
        self.actionSave_As.setObjectName("actionSave_As")
        self.actionUndo = QtWidgets.QAction(MainWindow)
        self.actionUndo.setObjectName("actionUndo")
        self.actionRedo = QtWidgets.QAction(MainWindow)
        self.actionRedo.setWhatsThis("")
        self.actionRedo.setObjectName("actionRedo")
        self.actionSlight_Randomizer = QtWidgets.QAction(MainWindow)
        self.actionSlight_Randomizer.setVisible(True)
        self.actionSlight_Randomizer.setObjectName("actionSlight_Randomizer")
        self.actionCrazy_Randomizer = QtWidgets.QAction(MainWindow)
        self.actionCrazy_Randomizer.setObjectName("actionCrazy_Randomizer")
        self.menuFile.addAction(self.actionUpload)
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionSave_As)
        self.menuEdit.addAction(self.actionUndo)
        self.menuEdit.addAction(self.actionRedo)
        self.menuRandomize.addAction(self.actionSlight_Randomizer)
        self.menuRandomize.addAction(self.actionCrazy_Randomizer)
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
        self.actionSave.setText(_translate("MainWindow", "Save"))
        self.actionSave.setStatusTip(_translate("MainWindow", "Saves image to existing file (assuming it exists)"))
        self.actionSave.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.actionSave_As.setText(_translate("MainWindow", "Save As"))
        self.actionSave_As.setStatusTip(_translate("MainWindow", "Saves image as new image file"))
        self.actionUndo.setText(_translate("MainWindow", "Undo"))
        self.actionUndo.setStatusTip(_translate("MainWindow", "Undos previous action"))
        self.actionUndo.setShortcut(_translate("MainWindow", "Ctrl+Z"))
        self.actionRedo.setText(_translate("MainWindow", "Redo"))
        self.actionRedo.setStatusTip(_translate("MainWindow", "Redos last action"))
        self.actionRedo.setShortcut(_translate("MainWindow", "Ctrl+Shift+Z"))
        self.actionSlight_Randomizer.setText(_translate("MainWindow", "Slight Randomizer"))
        self.actionSlight_Randomizer.setStatusTip(_translate("MainWindow", "Slightly randomizes current photo. More accurately resembles realistic training data."))
        self.actionSlight_Randomizer.setShortcut(_translate("MainWindow", "Ctrl+R"))
        self.actionCrazy_Randomizer.setText(_translate("MainWindow", "Crazy Randomizer"))
        self.actionCrazy_Randomizer.setStatusTip(_translate("MainWindow", "Completely randomizes every metric. Not very realistic."))

        # All actions:
        self.actionUpload.triggered.connect(self.importImage)
        self.RotateButton.clicked.connect(self.rotateNinety)
        self.VerticalFlipButton.clicked.connect(self.verticalFlip)
        self.HorizontalFlipButton.clicked.connect(self.horizontalFlip)
        self.GrayScaleButton.clicked.connect(self.greyscale)
        self.BrightnessSlider.valueChanged.connect(self.brightness)
        self.BrightnessSlider.sliderReleased.connect(self.brightnessReleased)
        self.ContrastSlider.valueChanged.connect(self.contrast)
        self.ContrastSlider.sliderReleased.connect(self.contrastReleased)
        self.SharpnessSlider.valueChanged.connect(self.sharpen)
        self.SharpnessSlider.sliderReleased.connect(self.sharpenReleased)
        self.SaturationSlider.valueChanged.connect(self.saturate)
        self.SaturationSlider.sliderReleased.connect(self.saturateReleased)
        self.BlurSlider.valueChanged.connect(self.blur)
        self.BlurSlider.sliderReleased.connect(self.blurReleased)
        self.RotateSlider.valueChanged.connect(self.rotate)
        self.RotateSlider.sliderReleased.connect(self.rotateReleased)
        self.PixelateSlider.valueChanged.connect(self.pixelate)
        self.PixelateSlider.sliderReleased.connect(self.pixelateReleased)

    def importImage(self):
        file_name, _ = QFileDialog.getOpenFileName() 
        self.pointer += 1
        self.PILHistory.append(Image.open(file_name))
        self.resizePhotoLabel(self.PILHistory[self.pointer])
        self.PhotoLabel.setPixmap(self.PILtoPIX(self.PILHistory[self.pointer]))


        # set to default
        self.BrightnessSlider.setSliderPosition(10)
        self.SharpnessSlider.setSliderPosition(0)
        self.SaturationSlider.setSliderPosition(10)
        self.ContrastSlider.setSliderPosition(10)
        self.RotateSlider.setSliderPosition(90)
        self.PixelateSlider.setSliderPosition(0)
        self.BlurSlider.setSliderPosition(0)

    # binary
    def rotateNinety(self):
        rotate_image = self.PILHistory[self.pointer].rotate(90, Image.Resampling.NEAREST, expand = 1)
        self.pointer += 1
        self.PILHistory.append(rotate_image)
        self.resizePhotoLabel(self.PILHistory[self.pointer])
        self.PhotoLabel.setPixmap(self.PILtoPIX(self.PILHistory[self.pointer]))   

    def verticalFlip(self):
        vertical_image = self.PILHistory[self.pointer].transpose(Image.Transpose.FLIP_TOP_BOTTOM)
        self.pointer += 1
        self.PILHistory.append(vertical_image)
        self.PhotoLabel.setPixmap(self.PILtoPIX(self.PILHistory[self.pointer]))   

    def horizontalFlip(self):
        horizontal_image = self.PILHistory[self.pointer].transpose(Image.Transpose.FLIP_LEFT_RIGHT)
        self.pointer += 1
        self.PILHistory.append(horizontal_image)
        self.PhotoLabel.setPixmap(self.PILtoPIX(self.PILHistory[self.pointer]))   

    def greyscale(self):
        # greyscale_image = self.PILHistory[self.pointer]
        greyscale_image = ImageOps.grayscale(self.PILHistory[self.pointer])
        self.pointer += 1
        self.PILHistory.append(greyscale_image)
        self.PhotoLabel.setPixmap(self.PILtoPIX(self.PILHistory[self.pointer]))  

    # dynamic
    def brightness(self):
        # print(self.BrightnessSlider.value())
        bright_image = ImageEnhance.Brightness(self.PILHistory[self.pointer])
        bright_image = bright_image.enhance(self.BrightnessSlider.value() / 10)
        self.PhotoLabel.setPixmap(self.PILtoPIX(bright_image)) 

    def brightnessReleased(self):
        bright_image = ImageEnhance.Brightness(self.PILHistory[self.pointer])
        bright_image = bright_image.enhance(self.BrightnessSlider.value() / 10)
        self.pointer += 1
        self.PILHistory.append(bright_image)

    def contrast(self):
        contrast_image = ImageEnhance.Contrast(self.PILHistory[self.pointer])
        contrast_image = contrast_image.enhance(self.ContrastSlider.value() / 10)
        self.PhotoLabel.setPixmap(self.PILtoPIX(contrast_image)) 

    def contrastReleased(self):
        contrast_image = ImageEnhance.Contrast(self.PILHistory[self.pointer])
        contrast_image = contrast_image.enhance(self.ContrastSlider.value() / 10)
        self.pointer += 1
        self.PILHistory.append(contrast_image)

    def sharpen(self):
        sharpen_image = ImageEnhance.Sharpness(self.PILHistory[self.pointer])
        sharpen_image = sharpen_image.enhance(self.SharpnessSlider.value() / 10)
        self.PhotoLabel.setPixmap(self.PILtoPIX(sharpen_image)) 

    def sharpenReleased(self):
        sharpen_image = ImageEnhance.Sharpness(self.PILHistory[self.pointer])
        sharpen_image = sharpen_image.enhance(self.SharpnessSlider.value() / 10)
        self.pointer += 1
        self.PILHistory.append(sharpen_image)

    def saturate(self):
        saturate_image = ImageEnhance.Color(self.PILHistory[self.pointer])
        saturate_image = saturate_image.enhance(self.SaturationSlider.value() / 10)
        self.PhotoLabel.setPixmap(self.PILtoPIX(saturate_image)) 

    def saturateReleased(self):
        sharpen_image = ImageEnhance.Color(self.PILHistory[self.pointer])
        sharpen_image = sharpen_image.enhance(self.SaturationSlider.value() / 10)
        self.pointer += 1
        self.PILHistory.append(sharpen_image)

    def blur(self):
        blur_image = self.PILHistory[self.pointer].filter(ImageFilter.GaussianBlur(radius = self.BlurSlider.value()))
        self.PhotoLabel.setPixmap(self.PILtoPIX(blur_image)) 

    def blurReleased(self):
        blur_image = self.PILHistory[self.pointer].filter(ImageFilter.GaussianBlur(radius = self.BlurSlider.value()))
        self.pointer += 1
        self.PILHistory.append(blur_image)

    def rotate(self):
        rotate_image = self.PILHistory[self.pointer].rotate(self.RotateSlider.value() - 90, Image.Resampling.NEAREST, expand = 1)
        self.resizePhotoLabel(rotate_image)
        self.PhotoLabel.setPixmap(self.PILtoPIX(rotate_image)) 

    def rotateReleased(self):
        rotate_image = self.PILHistory[self.pointer].rotate(self.RotateSlider.value() - 90, Image.Resampling.NEAREST, expand = 1)
        self.pointer += 1
        self.PILHistory.append(rotate_image)  

    def pixelate(self):
        original_image = self.PILHistory[self.pointer]
        original_size = original_image.size
        small_image = original_image.resize((int(original_size[0] / self.PixelateSlider.value()), int(original_size[1] / self.PixelateSlider.value())), Image.Resampling.BILINEAR)
        result_image = small_image.resize(original_size, Image.Resampling.NEAREST)
        self.PhotoLabel.setPixmap(self.PILtoPIX(result_image)) 

    def pixelateReleased(self):
        original_image = self.PILHistory[self.pointer]
        original_size = original_image.size
        small_image = original_image.resize((int(original_size[0] / self.PixelateSlider.value()), int(original_size[1] / self.PixelateSlider.value())), Image.Resampling.BILINEAR)
        result_image = small_image.resize(original_size, Image.Resampling.NEAREST)
        self.pointer += 1
        self.PILHistory.append(result_image)

    # Misc
    def storeInstruction(self, instruction, value):
        '''
        0. rotate ninety
        1. vertical flip
        2. horizontal flip
        3. greyscale
        4. brightness (scale)
        5. contrast (scale)
        6. sharpen (scale)
        7. saturate (scale)
        8. blur (scale)
        9. rotate (scale)
        10. pixelate (scale)
        '''
        # if instruction == "rotate ninety"
        pass

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
