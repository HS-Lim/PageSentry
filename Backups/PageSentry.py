from PyQt5.QtWidgets import (
        QApplication, QDialog, QMainWindow, QTableWidget, QTableWidgetItem
)
from PyQt5.QtCore import QObject
from ui_edit_window import Ui_EditWindow
from ui_about_window import Ui_AboutWindow
from ui_main_window import Ui_MainWindow
from ui_options_window import Ui_OptionsWindow
import sys

TITLE_COL = 0
INTERVAL_COL = 1
STATUS_COL = 2
WEBPAGE_COL = 3
    
class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        
        editWindow = EditWindow()
        editWindow.setModal(True)

        self.setupUi(self)

        self.newButton.clicked.connect(lambda: self.addNewAlert())
        self.editButton.clicked.connect(lambda: self.showEdit(editWindow))
        self.deleteButton.clicked.connect(lambda: self.deleteAlert())
        self.runButton.clicked.connect(lambda: self.toggleAlert())
        self.logButton.clicked.connect(lambda: self.showLog())

        self.actionAbout.triggered.connect(lambda: self.showAbout())
        self.actionOptions.triggered.connect(lambda: self.showOptions())
        self.actionNew.triggered.connect(lambda: self.addNewAlert())
        self.actionExit.triggered.connect(lambda: QApplication.quit())

        self.alertTableWidget.itemSelectionChanged.connect(lambda: self.enableTableActions())
        self.alertTableWidget.doubleClicked.connect(lambda: self.showEdit(editWindow))

        editWindow.editDialog.accepted.connect(
                lambda: self.applyEdit(editWindow))
        editWindow.editDialog.rejected.connect(
                lambda: self.discardEdit(editWindow))

        optionsWindow = OptionsWindow()
        optionsWindow.setModal(True)

        aboutWindow = AboutWindow()
        aboutWindow.setModal(True)

    def discardEdit(self, editWindow):
        pass

    def applyEdit(self, editWindow):
        title = editWindow.titleLineEdit.text()
        webpage = editWindow.webpageLineEdit.text()
        interval = editWindow.intervalLineEdit.text()
        timeUnit = editWindow.intervalComboBox.currentText()
        comboTime = (interval + " " + timeUnit)

        currRow = self.alertTableWidget.currentRow()

        self.alertTableWidget.item(currRow, TITLE_COL).setText(title)
        self.alertTableWidget.item(currRow, INTERVAL_COL).setText(comboTime)
        self.alertTableWidget.item(currRow, WEBPAGE_COL).setText(webpage)

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

    def generateNewAlertItems(self, row):
        toReturn = []

        toReturn.append(QTableWidgetItem("New Alert"))
        toReturn.append(QTableWidgetItem("1 Minute(s)"))
        toReturn.append(QTableWidgetItem("Inactive"))
        toReturn.append(QTableWidgetItem("http://google.com"))

        return toReturn

    def deleteAlert(self):
        self.alertTableWidget.removeRow(self.alertTableWidget.currentRow())

    def showAbout(self):
        aboutWindow = AboutWindow()
        aboutWindow.setModal(True)
        aboutWindow.exec()

    def showOptions(self):
        optionsWindow = OptionsWindow()
        optionsWindow.setModal(True)
        optionsWindow.exec()

    def showEdit(self, editWindow):
        currRow = self.alertTableWidget.currentRow()

        title = self.alertTableWidget.item(currRow, TITLE_COL).text()
        comboTime = self.alertTableWidget.item(currRow, INTERVAL_COL).text()
        webpage = self.alertTableWidget.item(currRow, WEBPAGE_COL).text()

        interval = comboTime.split()[0]
        timeUnit = comboTime.split()[1]

        editWindow.titleLineEdit.setText(title)
        editWindow.intervalLineEdit.setText(interval)
        comboIndex = editWindow.intervalComboBox.findText(timeUnit)
        editWindow.intervalComboBox.setCurrentIndex(comboIndex)
        editWindow.webpageLineEdit.setText(webpage)

        editWindow.exec()

    def toggleAlert(self):
        currRow = self.alertTableWidget.currentRow()

        currItem = self.alertTableWidget.item(currRow, STATUS_COL)

        if currItem.text() == "Inactive":
            currItem.setText("Active")
        elif currItem.text() == "Active":
            currItem.setText("Inactive")

    def showLog(self):
        #TODO: Open a text file with logged info
        pass

class EditWindow(QDialog, Ui_EditWindow):
    def __init__(self):
        super(EditWindow, self).__init__()

        #Unnecessary code? Accepted is a signal - use it to change main window.
        #self.editDialog.accepted.connect(lambda: self.saveEdit())
        #self.editDialog.rejected.connect(lambda: self.discardEdit())

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

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()

    window.show()
    sys.exit(app.exec_())
