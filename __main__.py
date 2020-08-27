from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtPrintSupport import QPrintDialog
from stylesheets.stylesheets import *
from dialogs.go_to_dialog import GoToDialog
from dialogs.find_dialog import FindDialog
from gui.main_window_gui_creation import main_create_gui

import resources
import time
import datetime


class TextEditMainWindow(QMainWindow):

    def __init__(self):
        QMainWindow.__init__(self)

        main_create_gui(self)

    # ==================================== GENERAL FUNCTIONALITY METHODS BELOW ====================================

    # --------------------------------------- 'NEW' ACTION ----------------------------------------

    def new_file(self):
        # creating pop-up window to check if user wants to save current file before opening new one
        question_box = QMessageBox.question(self, 'Boro text editor', 'Do you want to save current file?',
                                            QMessageBox.Yes | QMessageBox.No)
        # if user wants to save current file safe_file() method is run and the
        # text field/path are reverted to default state as we have opened new file
        if question_box == QMessageBox.Yes:
            self.save_file()
            self.file_path = None
            self.text_edit_field.setPlainText('')
            self.setWindowTitle(self.default_file_name + '.txt')
        # if not, text field/path are reverted to current stage
        elif question_box == QMessageBox.No:
            self.file_path = None
            self.text_edit_field.setPlainText('')
            self.setWindowTitle(self.default_file_name + '.txt')

    # --------------------------------------- 'NEW WINDOW' ACTION ----------------------------------------

    @staticmethod
    def new_window():
        new_window = TextEditMainWindow()
        new_window.setStyleSheet(style_sheet_graphite)
        new_window.show()

    # --------------------------------------- 'OPEN' ACTION ----------------------------------------

    def open_file(self):

        # define the file path by means of a dialog window
        path = QFileDialog.getOpenFileName(None, 'Open file', '', 'Text documents (*.txt)')[0]

        if path:
            # populate the text field with contents of file, update path and update window title
            with open(path, 'r') as file:
                text = file.read()
            self.text_edit_field.setPlainText(text)
            self.file_path = path
            self.setWindowTitle(path)

        # in case 'cancel' is selected in the dialog window
        else:
            return

    # --------------------------------------- 'SAVE' ACTION ----------------------------------------

    def save_file(self):
        # if self.path is empty i.e. we are not working on any existing file currently
        # function save_file_as() will be run for the user to create the path and file name
        if self.file_path is None:
            return self.save_file_as()

        self.save_to_path(self.file_path)

    def save_file_as(self):
        # QFileDialog opened to acquire new file path and name
        path = QFileDialog.getSaveFileName(None, 'Save file', self.default_file_name, 'Text documents (*.txt)')[0]

        # if 'cancel' is clicked the function terminates
        if not path:
            return

        self.save_to_path(path)

    def save_to_path(self, path):
        # creating a str object using the contents of the TextEdit
        text = self.text_edit_field.toPlainText()

        # context editor to create new file
        with open(path, 'w') as file:
            # contents of TextEdit written in the new file using write() builtin method
            file.write(text)

        # updating file path
        self.file_path = path
        # updating the window title to match currently edited file
        self.setWindowTitle(self.file_path)

    # --------------------------------------- 'PRINT' ACTION ----------------------------------------

    def print_file(self):
        # calling the qprintdialog class with 1st argument being the default printer, the second being the parent widget
        print_dialog = QPrintDialog(self.printer, self)
        if QDialog.Accepted == print_dialog.exec_():
            self.text_edit_field.print(self.printer)

    # --------------------------------------- 'PAGE SETUP' ACTION ----------------------------------------

    def page_setup(self):
        # calling the page setup dialog with 1st argument being the printer object and the second the parent widget
        print_setup_dialog = QPageSetupDialog(self.printer, self)
        print_setup_dialog.exec_()

    # --------------------------------------- 'EXIT' ACTION ----------------------------------------

    # overriding the built in closeEvent method to run the save_file method if the user chooses
    def closeEvent(self, event):
        # creating pop-up window containing two buttons Yes/No
        question_box = QMessageBox.question(self, 'Exit', 'Do you want to save before exiting?',
                                            QMessageBox.Yes | QMessageBox.No)

        # by clicking one of the buttons an outcome is created
        # if the outcome is Yes, before program is terminated the save_file() method will be run:
        if question_box == QMessageBox.Yes:
            self.save_file()
            event.accept()
        else:
            event.accept()

    # --------------------------------------- 'DATE/TIME' ACTION ----------------------------------------

    def date_time(self):
        # retrieving current date and time into a datetime object
        timestamp = datetime.datetime.now()
        # turning the datetime object into a string of given format and inserting into the text field at cursor location
        self.text_edit_field.insertPlainText(timestamp.strftime('%H:%M %d/%m/%Y'))

    # ---------------------------------------- 'ZOOM' ACTION ----------------------------------------

    def zoom_in(self):
        # using the built in zoomIn() and zoomOut() gui of the TextEdit object
        # to zoom in if current zoom not exceeding the borderline values
        if self.current_zoom < 500:
            self.text_edit_field.zoomIn(1)
            self.current_zoom += 10
            # updating the status bar display
            self.zoom_display.setText('Zoom: ' + str(self.current_zoom) + '%')

    def zoom_out(self):
        if self.current_zoom > 10:
            self.text_edit_field.zoomOut(1)
            self.current_zoom -= 10
            # updating the status bar display
            self.zoom_display.setText('Zoom: ' + str(self.current_zoom) + '%')

    # --------------------------------------- 'FONT' ACTION ----------------------------------------

    def font_selection(self):
        # using the built in getFont() method of QFontDialog class
        # to retrieve 1: the font, 2: a True boolean when the font is selected
        font, ok = QFontDialog.getFont()
        if ok:
            self.text_edit_field.setFont(font)

    # --------------------------------------- 'WRAP TEXT' ACTION ----------------------------------------

    def set_text_wrapping(self, action):
        # if the action passed as arg is checked (as it was set as checkable)
        # the line wrap mode for the text field is changed accordingly
        if action.isChecked():
            self.text_edit_field.setLineWrapMode(1)
        else:
            self.text_edit_field.setLineWrapMode(0)

    # ---------------------------------------- CURRENT COL/ROW UPDATE ACTION ----------------------------------------

    def current_column_row_update(self):
        # creating value containing the current text cursor of the text edit field
        cursor = self.text_edit_field.textCursor()
        # updating the value of current column/row using the built-in columnNumber() method
        # and the blockNumber() gui of the cursor object
        self.current_column = cursor.columnNumber()
        self.current_row = cursor.blockNumber()
        # updating the row/column display
        self.row_col_display.setText('Col: ' + str(self.current_column) + ', Row: ' + str(self.current_row) + ';')

    # ---------------------------------------- TOOLBAR DISPLAY ACTION ----------------------------------------

    def tool_bar_display(self, action):
        if action.isChecked():
            self.tool_bar.setVisible(True)
        else:
            self.tool_bar.setVisible(False)

    # ---------------------------------------- GOOGLE SEARCH ACTION ----------------------------------------

    def google_search(self):
        current_selection = self.text_edit_field.textCursor()
        searched_phrase = current_selection.selectedText().replace(' ', '+')
        url = QUrl('http://www.google.com/search?&q=' + searched_phrase)
        if not QDesktopServices.openUrl(url):
            MessageBox.warning(self, 'Google search', 'Could not open url')

    # ---------------------------------------- COLOR SCHEME CHANGE ACTION ----------------------------------------

    def color_scheme_change(self):
        if self.color_scheme_selector.currentText() == 'Graphite':
            self.style_sheet = style_sheet_graphite
            self.setStyleSheet(self.style_sheet)
        elif self.color_scheme_selector.currentText() == 'Sandstorm':
            self.style_sheet = style_sheet_sandstorm
            self.setStyleSheet(self.style_sheet)

    # ---------------------------------------- FIND ACTION ----------------------------------------

    @staticmethod
    def find_phrase(parent):
        find_dialog = FindDialog(parent)
        find_dialog.exec_()

    # ---------------------------------------- GOTO ACTION ----------------------------------------

    @staticmethod
    def go_to_row(parent):
        go_to_dialog = GoToDialog(parent)
        go_to_dialog.exec_()


if __name__ == '__main__':
    # encapsulating application in a variable
    editor = QApplication([])
    # setting application name
    editor.setApplicationName('Boro text editor')
    # setting app icon
    editor.setWindowIcon(QIcon('://icon_program.png'))
    # creating main app window
    main_window = TextEditMainWindow()
    # creating splash image using QPixmap class
    splash_image = QPixmap('://splash_screen.jpg')
    # creating the splash screen passing the image as argument
    splash_screen = QSplashScreen(splash_image)
    # showing the splash screen before the main window
    splash_screen.show()
    # two second delay to take in the splash screen
    time.sleep(2)
    # showing the main window
    main_window.show()
    # closing the splash screen using the finish() statement with main window as argument
    splash_screen.finish(main_window)
    # executing the app
    editor.exec_()
