from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtPrintSupport import *
from stylesheets.stylesheets import *
from dialogs.go_to_dialog import GoToDialog
from dialogs.find_dialog import FindDialog

import resources
import locale
import time
import datetime
import resources


class TextEditMainWindow(QMainWindow):

    def __init__(self):
        QMainWindow.__init__(self)

        # setting main window size (latter two args) and position on the monitor (first two args)
        self.setGeometry(200, 100, 700, 500)
        # setting attributes for the status bar
        self.current_column = 0
        self.current_row = 0
        self.current_zoom = 100
        self.current_language = locale.getdefaultlocale()[0][-2:]
        # creating the default printer object storing printing/page settings so that they can be later edited
        self.printer = QPrinter()
        # setting default style sheet
        self.style_sheet = style_sheet_graphite
        self.setStyleSheet(self.style_sheet)
        # creating the main text edit field
        self.text_edit_field = QPlainTextEdit()
        self.text_edit_field.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.text_edit_field.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.text_edit_field.setLineWrapMode(0)
        self.text_edit_field.cursorPositionChanged.connect(self.current_column_row_update)
        # defining default font and applying to the text edit field
        self.default_font = QFont('Consolas', 15)
        self.text_edit_field.setFont(self.default_font)
        # setting the text edit field as central widget
        self.setCentralWidget(self.text_edit_field)
        # attribute which will enable us to work on an opened file.
        # None by default as no file open when exe.
        self.file_path = None
        # attrib indicating default file name when saving etc.
        self.default_file_name = 'New_text_file'

        # ---------------------------------------- STATUS BAR ----------------------------------------

        # creating the status bar
        status_bar = QStatusBar(self)
        status_bar.setSizeGripEnabled(True)
        self.setStatusBar(status_bar)
        # creating the display of current zoom on the status bar
        self.zoom_display = QLineEdit('Zoom: ' + str(self.current_zoom) + '%')
        self.zoom_display.setReadOnly(True)
        self.zoom_display.setFixedWidth(80)
        self.zoom_display.setAlignment(Qt.AlignCenter)
        # adding the zoom display widget to the status bar
        status_bar.addPermanentWidget(self.zoom_display)
        # creating the display of current column and row
        self.row_col_display = QLineEdit('Col: ' + str(self.current_column) + ', Row: ' + str(self.current_row) + ';')
        self.row_col_display.setReadOnly(True)
        self.row_col_display.setFixedWidth(130)
        self.row_col_display.setAlignment(Qt.AlignCenter)
        # adding the display of current column and row to the status bar
        status_bar.addPermanentWidget(self.row_col_display)
        # creating the display of current OS language selected
        self.language_display = QLineEdit(self.current_language)
        self.language_display.setFixedWidth(35)
        self.language_display.setReadOnly(True)
        self.language_display.setAlignment(Qt.AlignCenter)
        # adding the display of current language to the status bar
        status_bar.addPermanentWidget(self.language_display)
        # adding the combo-box for colour scheme selection
        status_bar.addWidget(QLabel('Color scheme: '))
        self.color_scheme_selector = QComboBox(self)
        self.color_scheme_selector.addItem('Graphite')
        self.color_scheme_selector.addItem('Sandstorm')
        self.color_scheme_selector.currentIndexChanged.connect(self.color_scheme_change)
        status_bar.addWidget(self.color_scheme_selector)

        # ---------------------------------------- TOOLBAR ----------------------------------------

        # creating the toolbar
        self.tool_bar = self.addToolBar('Toolbar')
        self.tool_bar.setMovable(True)
        self.tool_bar.setIconSize(QSize(45, 45))
        # creating 'new' button on toolbar
        new_tool_button = QAction('New', self)
        new_tool_button.setIcon(QIcon('://icon_new_action.png'))
        new_tool_button.setToolTip('New document  Ctrl+N')
        new_tool_button.triggered.connect(self.new_file)
        self.tool_bar.addAction(new_tool_button)
        # creating 'open' button on toolbar
        open_tool_button = QAction('Open', self)
        open_tool_button.setIcon(QIcon('://icon_open_action.png'))
        open_tool_button.setToolTip('Open document  Ctrl+O')
        open_tool_button.triggered.connect(self.open_file)
        self.tool_bar.addAction(open_tool_button)
        # creating 'save' button on toolbar
        save_tool_button = QAction('Save', self)
        save_tool_button.setIcon(QIcon('://icon_save_action.png'))
        save_tool_button.setToolTip('Save document  Ctrl+S')
        save_tool_button.triggered.connect(self.save_file)
        self.tool_bar.addAction(save_tool_button)
        # creating 'print' button on toolbar
        print_tool_button = QAction('Print', self)
        print_tool_button.setIcon(QIcon('://icon_print_action.png'))
        print_tool_button.setToolTip('Print document  Ctrl+P')
        print_tool_button.triggered.connect(self.print_file)
        self.tool_bar.addAction(print_tool_button)
        self.tool_bar.addSeparator()
        # creating 'undo' button on toolbar
        undo_tool_button = QAction('Undo', self)
        undo_tool_button.setIcon(QIcon('://icon_undo_action.png'))
        undo_tool_button.setToolTip('Undo  Ctrl+Z')
        undo_tool_button.triggered.connect(self.text_edit_field.undo)
        self.tool_bar.addAction(undo_tool_button)
        # creating 'redo' button on toolbar
        redo_tool_button = QAction('Redo', self)
        redo_tool_button.setIcon(QIcon('://icon_redo_action.png'))
        redo_tool_button.setToolTip('Redo  Ctrl+Y')
        redo_tool_button.triggered.connect(self.text_edit_field.redo)
        self.tool_bar.addAction(redo_tool_button)
        self.tool_bar.addSeparator()
        # creating 'copy' button on toolbar
        copy_tool_button = QAction('Copy', self)
        copy_tool_button.setIcon(QIcon('://icon_copy_action.png'))
        copy_tool_button.setToolTip('Copy selected  Ctrl+C')
        copy_tool_button.triggered.connect(self.text_edit_field.copy)
        self.tool_bar.addAction(copy_tool_button)
        # creating 'paste' button on toolbar
        paste_tool_button = QAction('Paste', self)
        paste_tool_button.setIcon(QIcon('://icon_paste_action.png'))
        paste_tool_button.setToolTip('Paste  Ctrl+V')
        paste_tool_button.triggered.connect(self.text_edit_field.paste)
        self.tool_bar.addAction(paste_tool_button)
        # creating 'cut' button on toolbar
        cut_tool_button = QAction('Cut', self)
        cut_tool_button.setIcon(QIcon('://icon_cut_action.png'))
        cut_tool_button.setToolTip('Cut selected  Ctrl+X')
        cut_tool_button.triggered.connect(self.text_edit_field.cut)
        self.tool_bar.addAction(cut_tool_button)

        # ---------------------------------------- MENU BAR ----------------------------------------

        # creating the menubar
        menu_bar = QMenuBar(self)
        menu_bar.setGeometry(QRect(0, 0, 700, 30))
        self.setMenuBar(menu_bar)

        # creating FILE menu on menubar
        file_menu = menu_bar.addMenu('File')
        # creating new action in file menu
        new_action = QAction('New', self)
        new_action.setShortcut('Ctrl+N')
        new_action.triggered.connect(self.new_file)
        file_menu.addAction(new_action)
        # crating new window action in file menu
        new_window_action = QAction('New window', self)
        new_window_action.setShortcut('Ctrl+Shift+N')
        new_window_action.triggered.connect(self.new_window)
        file_menu.addAction(new_window_action)
        file_menu.addSeparator()
        # creating open file action in file menu
        open_action = QAction('Open', self)
        open_action.setShortcut('Ctrl+O')
        open_action.triggered.connect(self.open_file)
        file_menu.addAction(open_action)
        # creating save file action in file menu
        save_action = QAction('Save', self)
        save_action.setShortcut('Ctrl+S')
        save_action.triggered.connect(self.save_file)
        file_menu.addAction(save_action)
        # creating save file as action in file menu
        save_as_action = QAction('Save as...', self)
        save_as_action.setShortcut('Ctrl+Shift+S')
        save_as_action.triggered.connect(self.save_file_as)
        file_menu.addAction(save_as_action)
        file_menu.addSeparator()
        # creating page setup action
        page_setup_action = QAction('Page setup', self)
        page_setup_action.triggered.connect(self.page_setup)
        file_menu.addAction(page_setup_action)
        # creating print file as action in file menu
        print_action = QAction('Print', self)
        print_action.setShortcut('Ctrl+P')
        print_action.triggered.connect(self.print_file)
        file_menu.addAction(print_action)
        file_menu.addSeparator()
        # creating exit file as action in file menu
        exit_action = QAction('Exit', self)
        exit_action.setShortcut('Ctrl+Q')
        exit_action.triggered.connect(self.close)
        file_menu.addAction(exit_action)

        # creating EDIT menu on menubar
        edit_menu = menu_bar.addMenu('Edit')
        # creating undo action
        undo_action = edit_menu.addAction('Undo')
        undo_action.setShortcut('Ctrl+Z')
        undo_action.triggered.connect(self.text_edit_field.undo)
        # creating redo action
        redo_action = edit_menu.addAction('Redo')
        redo_action.setShortcut('Ctrl+Y')
        redo_action.triggered.connect(self.text_edit_field.redo)
        edit_menu.addSeparator()
        # creating the copy action
        copy_action = edit_menu.addAction('Copy')
        copy_action.setShortcut('Ctrl+C')
        copy_action.triggered.connect(self.text_edit_field.copy)
        # creating the paste action
        paste_action = edit_menu.addAction('Paste')
        paste_action.setShortcut('Ctrl+V')
        paste_action.triggered.connect(self.text_edit_field.paste)
        # creating the cut action
        cut_action = edit_menu.addAction('Cut')
        cut_action.setShortcut('Ctrl+X')
        cut_action.triggered.connect(self.text_edit_field.cut)
        # creating the find action
        find_action = edit_menu.addAction('Find')
        find_action.setShortcut('Ctrl+F')
        find_action.triggered.connect(lambda: self.find_phrase(self))
        # creating the go to action
        go_to_action = edit_menu.addAction('Go to')
        go_to_action.setShortcut('Ctrl+G')
        go_to_action.triggered.connect(lambda: self.go_to_row(self))
        # creating the Search in Google action
        search_in_google_action = edit_menu.addAction('Search in Google')
        search_in_google_action.setShortcut('Ctrl+Shift+G')
        search_in_google_action.triggered.connect(self.google_search)
        edit_menu.addSeparator()
        # creating the clear action
        clear_all_action = edit_menu.addAction('Clear all')
        clear_all_action.setShortcut('Ctrl+DEL')
        clear_all_action.triggered.connect(self.text_edit_field.clear)
        # creating select all action
        select_all_action = edit_menu.addAction('Select all')
        select_all_action.setShortcut('Ctrl+A')
        select_all_action.triggered.connect(self.text_edit_field.selectAll)
        # creating date/time action to paste timestamp
        date_time_action = edit_menu.addAction('Date/Time')
        date_time_action.setShortcut('F5')
        date_time_action.triggered.connect(self.date_time)

        # creating the FORMAT menu on menubar
        format_menu = menu_bar.addMenu('Format')
        # creating font action
        font_action = format_menu.addAction('Font')
        font_action.triggered.connect(self.font_selection)
        # creating the WRAP TEXT action
        wrap_text_action = format_menu.addAction('Wrap text')
        wrap_text_action.setCheckable(True)
        wrap_text_action.triggered.connect(lambda: self.set_text_wrapping(wrap_text_action))

        # creating VIEW menu
        view_menu = menu_bar.addMenu('View')
        # creating zoom sub-menu
        zoom_submenu = view_menu.addMenu('Zoom')
        # creating zoom-in action, setting shortcut and adding to the submenu
        zoom_in_action = QAction('Zoom in', self)
        zoom_in_action.setShortcut('Ctrl++')
        zoom_in_action.triggered.connect(self.zoom_in)
        zoom_submenu.addAction(zoom_in_action)
        # creating zoom-out action, setting shortcut and adding to submenu
        zoom_out_action = QAction('Zoom out', self)
        zoom_out_action.setShortcut('Ctrl+-')
        zoom_out_action.triggered.connect(self.zoom_out)
        zoom_submenu.addAction(zoom_out_action)
        view_menu.addSeparator()
        # creating toolbar action
        toolbar_action = QAction('Toolbar', self)
        toolbar_action.setCheckable(True)
        toolbar_action.setChecked(True)
        toolbar_action.triggered.connect(lambda: self.tool_bar_display(toolbar_action))
        view_menu.addAction(toolbar_action)

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
        # using the built in zoomIn() and zoomOut() methods of the TextEdit object
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
        # and the blockNumber() methods of the cursor object
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
