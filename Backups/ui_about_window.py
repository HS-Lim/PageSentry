# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UIFiles/AboutWindow.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_AboutWindow(object):
    def setupUi(self, AboutWindow):
        AboutWindow.setObjectName("AboutWindow")
        AboutWindow.resize(400, 150)
        self.gridLayout = QtWidgets.QGridLayout(AboutWindow)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.authorLabel = QtWidgets.QLabel(AboutWindow)
        self.authorLabel.setObjectName("authorLabel")
        self.verticalLayout.addWidget(self.authorLabel, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.linkLabel = QtWidgets.QLabel(AboutWindow)
        self.linkLabel.setObjectName("linkLabel")
        self.verticalLayout.addWidget(self.linkLabel, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.versLabelPassive = QtWidgets.QLabel(AboutWindow)
        self.versLabelPassive.setObjectName("versLabelPassive")
        self.horizontalLayout.addWidget(self.versLabelPassive, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.versLabelActive = QtWidgets.QLabel(AboutWindow)
        self.versLabelActive.setObjectName("versLabelActive")
        self.horizontalLayout.addWidget(self.versLabelActive, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.updatedLabelPassive = QtWidgets.QLabel(AboutWindow)
        self.updatedLabelPassive.setObjectName("updatedLabelPassive")
        self.horizontalLayout_2.addWidget(self.updatedLabelPassive, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.updatedLabelActive = QtWidgets.QLabel(AboutWindow)
        self.updatedLabelActive.setObjectName("updatedLabelActive")
        self.horizontalLayout_2.addWidget(self.updatedLabelActive, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)

        self.retranslateUi(AboutWindow)
        QtCore.QMetaObject.connectSlotsByName(AboutWindow)

    def retranslateUi(self, AboutWindow):
        _translate = QtCore.QCoreApplication.translate
        AboutWindow.setWindowTitle(_translate("AboutWindow", "About"))
        self.authorLabel.setText(_translate("AboutWindow", "Created by Hee Su Lim"))
        self.linkLabel.setText(_translate("AboutWindow", "TODO: Add GitHub link here"))
        self.versLabelPassive.setText(_translate("AboutWindow", "Version:"))
        self.versLabelActive.setText(_translate("AboutWindow", "TODO: Put version here"))
        self.updatedLabelPassive.setText(_translate("AboutWindow", "Last updated:"))
        self.updatedLabelActive.setText(_translate("AboutWindow", "TODO: Put update date here"))

