# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './UIFiles/EditWindow.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_EditWindow(object):
    def setupUi(self, EditWindow):
        EditWindow.setObjectName("EditWindow")
        EditWindow.resize(500, 196)
        self.gridLayout_2 = QtWidgets.QGridLayout(EditWindow)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.intervalLineEdit = QtWidgets.QLineEdit(EditWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.intervalLineEdit.sizePolicy().hasHeightForWidth())
        self.intervalLineEdit.setSizePolicy(sizePolicy)
        self.intervalLineEdit.setInputMethodHints(QtCore.Qt.ImhNone)
        self.intervalLineEdit.setObjectName("intervalLineEdit")
        self.horizontalLayout_3.addWidget(self.intervalLineEdit)
        self.intervalComboBox = QtWidgets.QComboBox(EditWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.intervalComboBox.sizePolicy().hasHeightForWidth())
        self.intervalComboBox.setSizePolicy(sizePolicy)
        self.intervalComboBox.setObjectName("intervalComboBox")
        self.intervalComboBox.addItem("")
        self.intervalComboBox.addItem("")
        self.intervalComboBox.addItem("")
        self.horizontalLayout_3.addWidget(self.intervalComboBox)
        self.gridLayout.addLayout(self.horizontalLayout_3, 3, 1, 1, 1)
        self.intervalLabel = QtWidgets.QLabel(EditWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.intervalLabel.sizePolicy().hasHeightForWidth())
        self.intervalLabel.setSizePolicy(sizePolicy)
        self.intervalLabel.setObjectName("intervalLabel")
        self.gridLayout.addWidget(self.intervalLabel, 3, 0, 1, 1)
        self.editDialog = QtWidgets.QDialogButtonBox(EditWindow)
        self.editDialog.setOrientation(QtCore.Qt.Horizontal)
        self.editDialog.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.editDialog.setObjectName("editDialog")
        self.gridLayout.addWidget(self.editDialog, 5, 1, 1, 1)
        self.webpageLabel = QtWidgets.QLabel(EditWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.webpageLabel.sizePolicy().hasHeightForWidth())
        self.webpageLabel.setSizePolicy(sizePolicy)
        self.webpageLabel.setObjectName("webpageLabel")
        self.gridLayout.addWidget(self.webpageLabel, 1, 0, 1, 1)
        self.titleLabel = QtWidgets.QLabel(EditWindow)
        self.titleLabel.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.titleLabel.sizePolicy().hasHeightForWidth())
        self.titleLabel.setSizePolicy(sizePolicy)
        self.titleLabel.setObjectName("titleLabel")
        self.gridLayout.addWidget(self.titleLabel, 0, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.titleLineEdit = QtWidgets.QLineEdit(EditWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.titleLineEdit.sizePolicy().hasHeightForWidth())
        self.titleLineEdit.setSizePolicy(sizePolicy)
        self.titleLineEdit.setObjectName("titleLineEdit")
        self.horizontalLayout.addWidget(self.titleLineEdit)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 1, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.webpageLineEdit = QtWidgets.QLineEdit(EditWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.webpageLineEdit.sizePolicy().hasHeightForWidth())
        self.webpageLineEdit.setSizePolicy(sizePolicy)
        self.webpageLineEdit.setObjectName("webpageLineEdit")
        self.horizontalLayout_2.addWidget(self.webpageLineEdit)
        self.gridLayout.addLayout(self.horizontalLayout_2, 1, 1, 1, 1)
        self.intervalErrLabel = QtWidgets.QLabel(EditWindow)
        font = QtGui.QFont()
        font.setPointSize(7)
        self.intervalErrLabel.setFont(font)
        self.intervalErrLabel.setObjectName("intervalErrLabel")
        self.gridLayout.addWidget(self.intervalErrLabel, 4, 1, 1, 1)
        self.webpageErrLabel = QtWidgets.QLabel(EditWindow)
        font = QtGui.QFont()
        font.setPointSize(7)
        self.webpageErrLabel.setFont(font)
        self.webpageErrLabel.setObjectName("webpageErrLabel")
        self.gridLayout.addWidget(self.webpageErrLabel, 2, 1, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)
        self.intervalLabel.setBuddy(self.intervalLineEdit)
        self.webpageLabel.setBuddy(self.webpageLineEdit)
        self.titleLabel.setBuddy(self.titleLineEdit)

        self.retranslateUi(EditWindow)
        self.editDialog.accepted.connect(EditWindow.accept)
        self.editDialog.rejected.connect(EditWindow.reject)
        QtCore.QMetaObject.connectSlotsByName(EditWindow)

    def retranslateUi(self, EditWindow):
        _translate = QtCore.QCoreApplication.translate
        EditWindow.setWindowTitle(_translate("EditWindow", "Edit"))
        self.intervalComboBox.setItemText(0, _translate("EditWindow", "Second(s)"))
        self.intervalComboBox.setItemText(1, _translate("EditWindow", "Minute(s)"))
        self.intervalComboBox.setItemText(2, _translate("EditWindow", "Hour(s)"))
        self.intervalLabel.setText(_translate("EditWindow", "&Interval"))
        self.webpageLabel.setText(_translate("EditWindow", "Webpa&ge"))
        self.titleLabel.setText(_translate("EditWindow", "Title"))
        self.intervalErrLabel.setText(_translate("EditWindow", "Input a valid number - ex: \"5\" or \"24.25\""))
        self.webpageErrLabel.setText(_translate("EditWindow", "Input a valid address - ex: \"https://www.google.com\" or \"http://google.com\""))

