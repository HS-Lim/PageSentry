from PyQt5.QtWidgets import (
        QApplication, QDialog, QMainWindow, QTableWidget, QTableWidgetItem,
        QDialogButtonBox, QFileDialog, QDesktopWidget, QMessageBox
)
from PyQt5.QtCore import QObject, QSettings, QSize, QPoint, QTimer, Qt
from PyQt5.QtMultimedia import QSound
from ui_edit_window import Ui_EditWindow
from ui_about_window import Ui_AboutWindow
from ui_main_window import Ui_MainWindow
from ui_options_window import Ui_OptionsWindow

from htmldiffer import diff
from bs4 import BeautifulSoup

import sys, re, requests, time

#Vars for alertTableWidget column indices
TITLE_COL = 0
INTERVAL_COL = 1
STATUS_COL = 2
WEBPAGE_COL = 3

#Required for QSettings
MY_ORG = "HLSoft"
MY_NAME = "Hee Su Lim"

class EditWindow(QDialog, Ui_EditWindow):
    def __init__(self):
        super(EditWindow, self).__init__()

        self.setupUi(self)

    def saveEdit(self):
        emit 

class OptionsWindow(QDialog, Ui_OptionsWindow):
    def __init__(self):
        super(OptionsWindow, self).__init__()

        self.setupUi(self)

class AboutWindow(QDialog, Ui_AboutWindow):
    def __init__(self):
        super(AboutWindow, self).__init__()

        self.setupUi(self)
    
class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        
        #Instantiate secondary windows, set up UI from ui files:
        self.editWindow = EditWindow()
        self.editWindow.setModal(True)

        self.optionsWindow = OptionsWindow()
        self.optionsWindow.setModal(True)

        self.aboutWindow = AboutWindow()
        self.aboutWindow.setModal(True)

        self.setupUi(self)

        #System settings:
        self.readMainWindowSettings()
        self.readOptionsSettings()
        self.loadTable()

        #Some UI elements not implemented in Qt Designer:
        self.editWindow.intervalErrLabel.setHidden(True)
        self.editWindow.intervalErrLabel.setStyleSheet("QLabel { color : red; }")

        #Signals, slots, connections:
        self.newButton.clicked.connect(lambda: self.addNewAlert())
        self.editButton.clicked.connect(lambda: self.showEdit())
        self.deleteButton.clicked.connect(lambda: self.deleteAlert())
        self.runButton.clicked.connect(lambda: self.toggleAlert())
        self.logButton.clicked.connect(lambda: self.showLog())

        self.actionAbout.triggered.connect(lambda: self.showAbout())
        self.actionOptions.triggered.connect(lambda: self.showOptions())
        self.actionNew.triggered.connect(lambda: self.addNewAlert())
        self.actionSave.triggered.connect(lambda: self.saveTable())
        self.actionExit.triggered.connect(lambda: QApplication.quit())

        self.alertTableWidget.itemSelectionChanged.connect(lambda: self.enableTableActions())
        self.alertTableWidget.doubleClicked.connect(lambda: self.showEdit())

        self.editWindow.editDialog.accepted.connect(
                lambda: self.applyEdit())
        self.editWindow.intervalLineEdit.textEdited.connect(
                lambda: self.checkIntervalInput())

        self.optionsWindow.soundDirButton.clicked.connect(
                lambda: self.chooseSoundDir())
        self.optionsWindow.logDirButton.clicked.connect(
                lambda: self.chooseLogDir())
        self.optionsWindow.optionsDialog.accepted.connect(
                lambda: self.writeOptionsSettings())

    def saveTable(self):
        settings = QSettings(MY_ORG, MY_NAME)
        settings.beginWriteArray("entries")

        currTable = self.alertTableWidget
        
        for row in range(0, self.alertTableWidget.rowCount()):
            settings.setArrayIndex(row)

            settings.setValue("title", currTable.item(
                row, TITLE_COL).text())
            settings.setValue("interval", currTable.item(
                row, INTERVAL_COL).text())
            settings.setValue("status", currTable.item(
                row, STATUS_COL).text())
            settings.setValue("webpage", currTable.item(
                row, WEBPAGE_COL).text())

        settings.endArray()
        MainWindow.setSavedFalse.hasSaved = True

    def loadTable(self):
        settings = QSettings(MY_ORG, MY_NAME)
        numRows = settings.beginReadArray("entries")

        currTable = self.alertTableWidget

        for row in range(0, numRows):
            settings.setArrayIndex(row)
            self.alertTableWidget.insertRow(row)

            currTable.setItem(row, TITLE_COL, QTableWidgetItem(
                str(settings.value("title"))))
            currTable.setItem(row, INTERVAL_COL, QTableWidgetItem(
                str(settings.value("interval"))))
            currTable.setItem(row, STATUS_COL, QTableWidgetItem(
                str(settings.value("status"))))
            currTable.setItem(row, WEBPAGE_COL, QTableWidgetItem(
                str(settings.value("webpage"))))

        settings.endArray()

    def closeEvent(self, event):
        if not MainWindow.setSavedFalse.hasSaved:
            message = "Do you want to save your alerts before exiting?"
            reply = QMessageBox.question(
                    self, 'Message', message, QMessageBox.Yes, QMessageBox.No)

            if reply == QMessageBox.Yes:
                self.saveTable()

    def setSavedFalse():
        MainWindow.setSavedFalse.hasSaved = False
        pass

    setSavedFalse.hasSaved = True

    def writeOptionsSettings(self):
        settings = QSettings(MY_ORG, MY_NAME)
        settings.beginGroup("OptionsWindow")

        settings.setValue("startup", self.optionsWindow.startupBox.isChecked())
        settings.setValue("minimize", self.optionsWindow.minimizeBox.isChecked())
        settings.setValue("log", self.optionsWindow.logBox.isChecked())
        settings.setValue("sound", self.optionsWindow.soundBox.isChecked())
        settings.setValue("custom", self.optionsWindow.customBox.isChecked())

        print(settings.value("startup"))

        settings.setValue("logDir", self.optionsWindow.logLineEdit.text())
        settings.setValue("soundDir", self.optionsWindow.soundLineEdit.text())
        
        settings.endGroup()

    def readOptionsSettings(self):
        settings = QSettings(MY_ORG, MY_NAME)
        settings.beginGroup("OptionsWindow")

        #The parseBoolString is necessary as a result of ini files not storing
        #bool values, but turning them into strings "false", "true"
        self.optionsWindow.startupBox.setChecked(
                self.parseBoolString(settings.value("startup", False)))
        self.optionsWindow.minimizeBox.setChecked(
                self.parseBoolString(settings.value("minimize", False)))
        self.optionsWindow.logBox.setChecked(
                self.parseBoolString(settings.value("log", False)))
        self.optionsWindow.soundBox.setChecked(
                self.parseBoolString(settings.value("sound", False)))
        self.optionsWindow.customBox.setChecked(
                self.parseBoolString(settings.value("custom", False)))

        self.optionsWindow.logLineEdit.setText(settings.value("logDir", ""))
        self.optionsWindow.soundLineEdit.setText(settings.value("soundDir", ""))

        settings.endGroup()

    def parseBoolString(self, myStr):
        if type(myStr) == bool:
            return myStr
        return myStr[0].upper() == 'T'

    def __restoreWindowDefaults__(self):
        settings = QSettings(MY_ORG, MY_NAME)
        settings.beginGroup("MainWindow")
        settings.setValue("size", QSize(800, 600))
        
        qtRectangle = self.frameGeometry()
        centerPoint = QDesktopWidget().availableGeometry().center()
        qtRectangle.moveCenter(centerPoint)
        
        settings.setValue("pos", qtRectangle.topLeft())
        settings.endGroup()

    def writeMainWindowSettings(self):
        settings = QSettings(MY_ORG, MY_NAME)
        settings.beginGroup("MainWindow")
        #Window settings
        settings.setValue("size", self.size())
        settings.setValue("pos", self.pos())

        #Table Column sizes settings
        table = self.alertTableWidget
        settings.setValue("widthTitle", table.columnWidth(TITLE_COL))
        settings.setValue("widthInterval", table.columnWidth(INTERVAL_COL))
        settings.setValue("widthStatus", table.columnWidth(STATUS_COL))
        settings.setValue("widthWebpage", table.columnWidth(WEBPAGE_COL))

        #print(table.columnWidth(TITLE_COL))
        #print(table.columnWidth(INTERVAL_COL))
        #print(table.columnWidth(STATUS_COL))
        #print(table.columnWidth(WEBPAGE_COL))

        settings.endGroup()

    def readMainWindowSettings(self):
        settings = QSettings(MY_ORG, MY_NAME)

        settings.beginGroup("MainWindow")
        self.resize(settings.value("size", QSize(800, 600)))
        
        #Grabs the position of the center of the screen for default window pos
        qtRectangle = self.frameGeometry()
        centerPoint = QDesktopWidget().availableGeometry().center()
        qtRectangle.moveCenter(centerPoint)

        self.move(settings.value("pos", qtRectangle.topLeft()))

        #Table column sizes settings, magic numbers are default values in px
        table = self.alertTableWidget
        table.setColumnWidth(
                TITLE_COL, int(settings.value("widthTitle", 150)))
        table.setColumnWidth(
                INTERVAL_COL, int(settings.value("widthInterval", 150)))
        table.setColumnWidth(
                STATUS_COL, int(settings.value("widthStatus",150)))
        table.setColumnWidth(
                WEBPAGE_COL, int(settings.value("widthWebpage", 350)))

        settings.endGroup()

    def chooseSoundDir(self):
        fileName = QFileDialog.getOpenFileName(
                self, "Open sound file", "", 
                "Sound Files (*.wav *.mp3 *.ogg *.flac)")[0]

        if fileName:
            self.optionsWindow.soundLineEdit.setText(fileName)

    def chooseLogDir(self):
        dirName = QFileDialog.getExistingDirectory(
                self, "Open log directory", "")

        if dirName:
            self.optionsWindow.logLineEdit.setText(dirName)

    def checkIntervalInput(self):
        try:
            float(self.editWindow.intervalLineEdit.text())
            self.editWindow.intervalErrLabel.setHidden(True)
            self.editWindow.editDialog.button(QDialogButtonBox.Ok).setEnabled(True)
        except ValueError:
            self.editWindow.intervalErrLabel.setHidden(False)
            self.editWindow.editDialog.button(QDialogButtonBox.Ok).setEnabled(False)

    def applyEdit(self): 
        title = self.editWindow.titleLineEdit.text()
        webpage = self.editWindow.webpageLineEdit.text()
        interval = self.editWindow.intervalLineEdit.text()
        timeUnit = self.editWindow.intervalComboBox.currentText()
        comboTime = (interval + " " + timeUnit)

        currRow = self.alertTableWidget.currentRow()

        self.alertTableWidget.item(currRow, TITLE_COL).setText(title)
        self.alertTableWidget.item(currRow, INTERVAL_COL).setText(comboTime)
        self.alertTableWidget.item(currRow, WEBPAGE_COL).setText(webpage)

        MainWindow.setSavedFalse()

    def enableTableActions(self):
        if len(self.alertTableWidget.selectedIndexes()) > 0:
            isRowSelected = True
        else:
            isRowSelected = False

        self.editButton.setEnabled(isRowSelected)
        self.deleteButton.setEnabled(isRowSelected)
        self.runButton.setEnabled(isRowSelected)

    def addNewAlert(self):
        currRow = self.alertTableWidget.rowCount()
        self.alertTableWidget.insertRow(currRow)

        tableItems = self.generateNewAlertItems(currRow)

        for column, item in enumerate(tableItems):
            self.alertTableWidget.setItem(currRow, column, item)

        MainWindow.setSavedFalse()

    def generateNewAlertItems(self, row):
        toReturn = []

        toReturn.append(QTableWidgetItem("New Alert"))
        toReturn.append(QTableWidgetItem("1 Minute(s)"))
        toReturn.append(QTableWidgetItem("Inactive"))
        toReturn.append(QTableWidgetItem("http://google.com"))

        return toReturn

    def deleteAlert(self):
        self.alertTableWidget.removeRow(self.alertTableWidget.currentRow())

        MainWindow.setSavedFalse()

    def showAbout(self):
        self.aboutWindow.setModal(True)
        self.aboutWindow.exec()

    def showOptions(self):
        self.optionsWindow.setModal(True)
        self.optionsWindow.exec()

    def showEdit(self):
        currRow = self.alertTableWidget.currentRow()

        title = self.alertTableWidget.item(currRow, TITLE_COL).text()
        comboTime = self.alertTableWidget.item(currRow, INTERVAL_COL).text()
        webpage = self.alertTableWidget.item(currRow, WEBPAGE_COL).text()

        interval = comboTime.split()[0]
        timeUnit = comboTime.split()[1]

        self.editWindow.titleLineEdit.setText(title)
        self.editWindow.intervalLineEdit.setText(interval)
        comboIndex = self.editWindow.intervalComboBox.findText(timeUnit)
        self.editWindow.intervalComboBox.setCurrentIndex(comboIndex)
        self.editWindow.webpageLineEdit.setText(webpage)

        self.checkIntervalInput()

        self.editWindow.exec()

    def toggleAlert(self):
        print(self.optionsWindow.soundLineEdit.text())
        QSound.play(self.optionsWindow.soundLineEdit.text())
        currRow = self.alertTableWidget.currentRow()

        currItem = self.alertTableWidget.item(currRow, STATUS_COL)
        if currItem.text() == "Inactive":
            currItem.setText("Active")
            self.startTimer(currRow)
        elif currItem.text() == "Active":
            currItem.setText("Inactive")
            self.endTimer(currRow)

    def startTimer(self, rowIndex):
        #Create a Qtimer that will signal to our scan/alert function
        timer = QTimer(self)
        timer.timeout.connect(lambda: self.runAlert(rowIndex))

        #We put data in the interval item of the given row that points to the
        #Qtimer associated with that alert, so that we can access the timer
        #given a row
        intervalItem = self.alertTableWidget.item(rowIndex, INTERVAL_COL)
        intervalItem.setData(Qt.UserRole, timer)
        
        #We store a None in the table to check if we're retrieving the page for
        #the first time when runAlert starts being called by QTimer
        webpageItem = self.alertTableWidget.item(rowIndex, WEBPAGE_COL)
        webpageItem.setData(Qt.UserRole, None)

        #Then we start the timer based on the interval specified by the user:
        tempInterval = self.alertTableWidget.item(rowIndex,
                INTERVAL_COL).text().split()

        intervalMS = self.convertToMS(tempInterval)
        timer.start(intervalMS)
        
        
    def getPageContent(self, address):
        response = requests.get(address)
        content = response.content

        soup = BeautifulSoup(content)

        return soup.prettify()

    def endTimer(self, rowIndex):
        timer = self.alertTableWidget.item(
                rowIndex, INTERVAL_COL).data(Qt.UserRole)
        timer.stop()

    def convertToMS(self, time):
        timeValue = time[0]
        timeUnit = time[1]
        if timeUnit == "Second(s)":
            return float(timeValue) * 1000
        elif timeUnit == "Minute(s)":
            return float(timeValue) * 1000 * 60
        elif timeUnit == "Hour(s)":
            return float(timeValue) * 1000 * 60 * 60
        
    def runAlert(self, rowIndex):
        print("Scanning")
        webpageItem = self.alertTableWidget.item(rowIndex, WEBPAGE_COL)

        #Get the current copy of the website we're checking:
        currContent = self.getPageContent(webpageItem.text())
        
        if webpageItem.data(Qt.UserRole) is None:
            webpageItem.setData(Qt.UserRole, currContent)
        elif currContent != webpageItem.data(Qt.UserRole):
            webpageItem.setData(Qt.UserRole, currContent)
            #TODO: Bring out the alarms, log, etc.
            print("ALEEEEEEEEEEERT")

            if self.optionsWindow.soundBox.isChecked():
                if self.optionsWindow.customBox.isChecked():
                    QSound.play(self.optionsWindow.soundLineEdit.text())
                else:
                    QSound.play("bell.wav")

    def showLog(self):
        #TODO: Open a text file with logged info
        pass

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()

    #On exit, write settings:
    app.aboutToQuit.connect(lambda: window.writeMainWindowSettings())

    window.show()
    sys.exit(app.exec_())
