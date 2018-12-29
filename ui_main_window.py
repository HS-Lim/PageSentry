# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './UIFiles/MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.alertTableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.alertTableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.alertTableWidget.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.alertTableWidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.alertTableWidget.setObjectName("alertTableWidget")
        self.alertTableWidget.setColumnCount(4)
        self.alertTableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.alertTableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.alertTableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.alertTableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.alertTableWidget.setHorizontalHeaderItem(3, item)
        self.alertTableWidget.horizontalHeader().setDefaultSectionSize(150)
        self.alertTableWidget.horizontalHeader().setSortIndicatorShown(False)
        self.alertTableWidget.horizontalHeader().setStretchLastSection(True)
        self.alertTableWidget.verticalHeader().setVisible(False)
        self.alertTableWidget.verticalHeader().setCascadingSectionResizes(False)
        self.gridLayout.addWidget(self.alertTableWidget, 0, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.newButton = QtWidgets.QPushButton(self.centralwidget)
        self.newButton.setObjectName("newButton")
        self.horizontalLayout.addWidget(self.newButton)
        self.editButton = QtWidgets.QPushButton(self.centralwidget)
        self.editButton.setEnabled(False)
        self.editButton.setObjectName("editButton")
        self.horizontalLayout.addWidget(self.editButton)
        self.deleteButton = QtWidgets.QPushButton(self.centralwidget)
        self.deleteButton.setEnabled(False)
        self.deleteButton.setObjectName("deleteButton")
        self.horizontalLayout.addWidget(self.deleteButton)
        self.runButton = QtWidgets.QPushButton(self.centralwidget)
        self.runButton.setEnabled(False)
        self.runButton.setFlat(False)
        self.runButton.setObjectName("runButton")
        self.horizontalLayout.addWidget(self.runButton)
        self.logButton = QtWidgets.QPushButton(self.centralwidget)
        self.logButton.setEnabled(True)
        self.logButton.setObjectName("logButton")
        self.horizontalLayout.addWidget(self.logButton)
        self.gridLayout_2.addLayout(self.horizontalLayout, 1, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 32))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuTools = QtWidgets.QMenu(self.menubar)
        self.menuTools.setObjectName("menuTools")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.actionNew_Entry = QtWidgets.QAction(MainWindow)
        self.actionNew_Entry.setObjectName("actionNew_Entry")
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.actionGithub = QtWidgets.QAction(MainWindow)
        self.actionGithub.setObjectName("actionGithub")
        self.actionOptions = QtWidgets.QAction(MainWindow)
        self.actionOptions.setObjectName("actionOptions")
        self.actionNew = QtWidgets.QAction(MainWindow)
        self.actionNew.setObjectName("actionNew")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")
        self.menuFile.addAction(self.actionNew)
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionExit)
        self.menuTools.addAction(self.actionOptions)
        self.menuHelp.addAction(self.actionAbout)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuTools.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "PageSentry"))
        item = self.alertTableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Title"))
        item = self.alertTableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Interval"))
        item = self.alertTableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Status"))
        item = self.alertTableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Webpage"))
        self.newButton.setText(_translate("MainWindow", "New"))
        self.editButton.setText(_translate("MainWindow", "Edit"))
        self.deleteButton.setText(_translate("MainWindow", "Delete"))
        self.runButton.setText(_translate("MainWindow", "Run / Pause"))
        self.logButton.setText(_translate("MainWindow", "Log"))
        self.menuFile.setTitle(_translate("MainWindow", "&File"))
        self.menuTools.setTitle(_translate("MainWindow", "&Tools"))
        self.menuHelp.setTitle(_translate("MainWindow", "&Help"))
        self.actionNew_Entry.setText(_translate("MainWindow", "&New Entry"))
        self.actionAbout.setText(_translate("MainWindow", "&About"))
        self.actionGithub.setText(_translate("MainWindow", "GitHub"))
        self.actionOptions.setText(_translate("MainWindow", "&Options"))
        self.actionNew.setText(_translate("MainWindow", "&New"))
        self.actionExit.setText(_translate("MainWindow", "&Exit"))
        self.actionSave.setText(_translate("MainWindow", "Save"))

