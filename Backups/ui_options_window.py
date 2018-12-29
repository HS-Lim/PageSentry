# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UIFiles/OptionsWindow.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_OptionsWindow(object):
    def setupUi(self, OptionsWindow):
        OptionsWindow.setObjectName("OptionsWindow")
        OptionsWindow.resize(500, 180)
        self.gridLayout = QtWidgets.QGridLayout(OptionsWindow)
        self.gridLayout.setObjectName("gridLayout")
        self.optionsDialog = QtWidgets.QDialogButtonBox(OptionsWindow)
        self.optionsDialog.setOrientation(QtCore.Qt.Horizontal)
        self.optionsDialog.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.optionsDialog.setObjectName("optionsDialog")
        self.gridLayout.addWidget(self.optionsDialog, 1, 0, 1, 1)
        self.frame = QtWidgets.QFrame(OptionsWindow)
        self.frame.setObjectName("frame")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.soundLocButton = QtWidgets.QPushButton(self.frame)
        self.soundLocButton.setEnabled(False)
        self.soundLocButton.setObjectName("soundLocButton")
        self.gridLayout_2.addWidget(self.soundLocButton, 3, 2, 1, 1)
        self.soundBox = QtWidgets.QCheckBox(self.frame)
        self.soundBox.setObjectName("soundBox")
        self.gridLayout_2.addWidget(self.soundBox, 3, 0, 1, 1)
        self.fileLineEdit = QtWidgets.QLineEdit(self.frame)
        self.fileLineEdit.setEnabled(False)
        self.fileLineEdit.setObjectName("fileLineEdit")
        self.gridLayout_2.addWidget(self.fileLineEdit, 3, 1, 1, 1)
        self.logCheckBox = QtWidgets.QCheckBox(self.frame)
        self.logCheckBox.setChecked(True)
        self.logCheckBox.setObjectName("logCheckBox")
        self.gridLayout_2.addWidget(self.logCheckBox, 1, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.startupBox = QtWidgets.QCheckBox(self.frame)
        self.startupBox.setObjectName("startupBox")
        self.horizontalLayout.addWidget(self.startupBox)
        self.updateBox = QtWidgets.QCheckBox(self.frame)
        self.updateBox.setObjectName("updateBox")
        self.horizontalLayout.addWidget(self.updateBox)
        self.minimizeBox = QtWidgets.QCheckBox(self.frame)
        self.minimizeBox.setObjectName("minimizeBox")
        self.horizontalLayout.addWidget(self.minimizeBox)
        self.gridLayout_2.addLayout(self.horizontalLayout, 0, 0, 1, 3)
        self.logLineEdit = QtWidgets.QLineEdit(self.frame)
        self.logLineEdit.setEnabled(False)
        self.logLineEdit.setObjectName("logLineEdit")
        self.gridLayout_2.addWidget(self.logLineEdit, 1, 1, 1, 1)
        self.logLocButton = QtWidgets.QPushButton(self.frame)
        self.logLocButton.setObjectName("logLocButton")
        self.gridLayout_2.addWidget(self.logLocButton, 1, 2, 1, 1)
        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)

        self.retranslateUi(OptionsWindow)
        self.optionsDialog.accepted.connect(OptionsWindow.accept)
        self.optionsDialog.rejected.connect(OptionsWindow.reject)
        QtCore.QMetaObject.connectSlotsByName(OptionsWindow)

    def retranslateUi(self, OptionsWindow):
        _translate = QtCore.QCoreApplication.translate
        OptionsWindow.setWindowTitle(_translate("OptionsWindow", "Options"))
        self.soundLocButton.setText(_translate("OptionsWindow", "Choose..."))
        self.soundBox.setText(_translate("OptionsWindow", "Custom sound:"))
        self.logCheckBox.setText(_translate("OptionsWindow", "Create log file at:"))
        self.startupBox.setText(_translate("OptionsWindow", "Run on startup"))
        self.updateBox.setText(_translate("OptionsWindow", "Auto update"))
        self.minimizeBox.setText(_translate("OptionsWindow", "Minimize to tray"))
        self.logLocButton.setText(_translate("OptionsWindow", "Choose..."))

