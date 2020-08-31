from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtPrintSupport import QPrinter
from src.stylesheets.stylesheets import *

import locale
import resources


# ---------------------------------------- CREATING MAIN GUI ----------------------------------------


def main_create_gui(window):
    # setting main window size (latter two args) and position on the monitor (first two args)
    window.setGeometry(200, 100, 700, 500)
    # setting attributes for the status bar
    window.current_column = 0
    window.current_row = 0
    window.current_zoom = 100
    window.current_language = locale.getdefaultlocale()[0][-2:]
    # creating the default printer object storing printing/page settings so that they can be later edited
    window.printer = QPrinter()
    # setting default style sheet
    window.style_sheet = style_sheet_graphite
    window.setStyleSheet(window.style_sheet)
    # creating the main text edit field
    window.text_edit_field = QPlainTextEdit()
    window.text_edit_field.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
    window.text_edit_field.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
    window.text_edit_field.setLineWrapMode(0)
    window.text_edit_field.cursorPositionChanged.connect(window.current_column_row_update)
    # defining default font and applying to the text edit field
    window.default_font = QFont('Consolas', 15)
    window.text_edit_field.setFont(window.default_font)
    # setting the text edit field as central widget
    window.setCentralWidget(window.text_edit_field)
    # attribute which will enable us to work on an opened file.
    # None by default as no file open when exe.
    window.file_path = None
    # attrib indicating default file name when saving etc.
    window.default_file_name = 'New_text_file'

# ---------------------------------------- CREATING STATUS BAR ----------------------------------------


def main_create_status_bar(window):
    status_bar = QStatusBar(window)
    status_bar.setSizeGripEnabled(True)
    window.setStatusBar(status_bar)
    # creating the display of current zoom on the status bar
    window.zoom_display = QLineEdit('Zoom: ' + str(window.current_zoom) + '%')
    window.zoom_display.setReadOnly(True)
    window.zoom_display.setFixedWidth(80)
    window.zoom_display.setAlignment(Qt.AlignCenter)
    # adding the zoom display widget to the status bar
    status_bar.addPermanentWidget(window.zoom_display)
    # creating the display of current column and row
    window.row_col_display = QLineEdit('Col: ' + str(window.current_column) + ', Row: ' + str(window.current_row) + ';')
    window.row_col_display.setReadOnly(True)
    window.row_col_display.setFixedWidth(130)
    window.row_col_display.setAlignment(Qt.AlignCenter)
    # adding the display of current column and row to the status bar
    status_bar.addPermanentWidget(window.row_col_display)
    # creating the display of current OS language selected
    window.language_display = QLineEdit(window.current_language)
    window.language_display.setFixedWidth(35)
    window.language_display.setReadOnly(True)
    window.language_display.setAlignment(Qt.AlignCenter)
    # adding the display of current language to the status bar
    status_bar.addPermanentWidget(window.language_display)
    # adding the combo-box for colour scheme selection
    status_bar.addWidget(QLabel('Color scheme: '))
    window.color_scheme_selector = QComboBox(window)
    window.color_scheme_selector.addItem('Graphite')
    window.color_scheme_selector.addItem('Sandstorm')
    window.color_scheme_selector.currentIndexChanged.connect(window.color_scheme_change)
    status_bar.addWidget(window.color_scheme_selector)

# ---------------------------------------- CREATING TOOLBAR ----------------------------------------


def main_create_toolbar(window):
    window.tool_bar = window.addToolBar('Toolbar')
    window.tool_bar.setMovable(True)
    window.tool_bar.setIconSize(QSize(45, 45))
    # creating 'new' button on toolbar
    new_tool_button = QAction('New', window)
    new_tool_button.setIcon(QIcon('://icon_new_action.png'))
    new_tool_button.setToolTip('New document  Ctrl+N')
    new_tool_button.triggered.connect(window.new_file)
    window.tool_bar.addAction(new_tool_button)
    # creating 'open' button on toolbar
    open_tool_button = QAction('Open', window)
    open_tool_button.setIcon(QIcon('://icon_open_action.png'))
    open_tool_button.setToolTip('Open document  Ctrl+O')
    open_tool_button.triggered.connect(window.open_file)
    window.tool_bar.addAction(open_tool_button)
    # creating 'save' button on toolbar
    save_tool_button = QAction('Save', window)
    save_tool_button.setIcon(QIcon('://icon_save_action.png'))
    save_tool_button.setToolTip('Save document  Ctrl+S')
    save_tool_button.triggered.connect(window.save_file)
    window.tool_bar.addAction(save_tool_button)
    # creating 'print' button on toolbar
    print_tool_button = QAction('Print', window)
    print_tool_button.setIcon(QIcon('://icon_print_action.png'))
    print_tool_button.setToolTip('Print document  Ctrl+P')
    print_tool_button.triggered.connect(window.print_file)
    window.tool_bar.addAction(print_tool_button)
    window.tool_bar.addSeparator()
    # creating 'undo' button on toolbar
    undo_tool_button = QAction('Undo', window)
    undo_tool_button.setIcon(QIcon('://icon_undo_action.png'))
    undo_tool_button.setToolTip('Undo  Ctrl+Z')
    undo_tool_button.triggered.connect(window.text_edit_field.undo)
    window.tool_bar.addAction(undo_tool_button)
    # creating 'redo' button on toolbar
    redo_tool_button = QAction('Redo', window)
    redo_tool_button.setIcon(QIcon('://icon_redo_action.png'))
    redo_tool_button.setToolTip('Redo  Ctrl+Y')
    redo_tool_button.triggered.connect(window.text_edit_field.redo)
    window.tool_bar.addAction(redo_tool_button)
    window.tool_bar.addSeparator()
    # creating 'copy' button on toolbar
    copy_tool_button = QAction('Copy', window)
    copy_tool_button.setIcon(QIcon('://icon_copy_action.png'))
    copy_tool_button.setToolTip('Copy selected  Ctrl+C')
    copy_tool_button.triggered.connect(window.text_edit_field.copy)
    window.tool_bar.addAction(copy_tool_button)
    # creating 'paste' button on toolbar
    paste_tool_button = QAction('Paste', window)
    paste_tool_button.setIcon(QIcon('://icon_paste_action.png'))
    paste_tool_button.setToolTip('Paste  Ctrl+V')
    paste_tool_button.triggered.connect(window.text_edit_field.paste)
    window.tool_bar.addAction(paste_tool_button)
    # creating 'cut' button on toolbar
    cut_tool_button = QAction('Cut', window)
    cut_tool_button.setIcon(QIcon('://icon_cut_action.png'))
    cut_tool_button.setToolTip('Cut selected  Ctrl+X')
    cut_tool_button.triggered.connect(window.text_edit_field.cut)
    window.tool_bar.addAction(cut_tool_button)

# ---------------------------------------- CREATING MENU BAR ----------------------------------------


def main_create_menu_bar(window):
    menu_bar = QMenuBar(window)
    menu_bar.setGeometry(QRect(0, 0, 700, 30))
    window.setMenuBar(menu_bar)

    # creating FILE menu on menubar
    file_menu = menu_bar.addMenu('File')
    # creating new action in file menu
    new_action = QAction('New', window)
    new_action.setShortcut('Ctrl+N')
    new_action.triggered.connect(window.new_file)
    file_menu.addAction(new_action)
    # crating new window action in file menu
    new_window_action = QAction('New window', window)
    new_window_action.setShortcut('Ctrl+Shift+N')
    new_window_action.triggered.connect(window.new_window)
    file_menu.addAction(new_window_action)
    file_menu.addSeparator()
    # creating open file action in file menu
    open_action = QAction('Open', window)
    open_action.setShortcut('Ctrl+O')
    open_action.triggered.connect(window.open_file)
    file_menu.addAction(open_action)
    # creating save file action in file menu
    save_action = QAction('Save', window)
    save_action.setShortcut('Ctrl+S')
    save_action.triggered.connect(window.save_file)
    file_menu.addAction(save_action)
    # creating save file as action in file menu
    save_as_action = QAction('Save as...', window)
    save_as_action.setShortcut('Ctrl+Shift+S')
    save_as_action.triggered.connect(window.save_file_as)
    file_menu.addAction(save_as_action)
    file_menu.addSeparator()
    # creating page setup action
    page_setup_action = QAction('Page setup', window)
    page_setup_action.triggered.connect(window.page_setup)
    file_menu.addAction(page_setup_action)
    # creating print file as action in file menu
    print_action = QAction('Print', window)
    print_action.setShortcut('Ctrl+P')
    print_action.triggered.connect(window.print_file)
    file_menu.addAction(print_action)
    file_menu.addSeparator()
    # creating exit file as action in file menu
    exit_action = QAction('Exit', window)
    exit_action.setShortcut('Ctrl+Q')
    exit_action.triggered.connect(window.close)
    file_menu.addAction(exit_action)

    # creating EDIT menu on menubar
    edit_menu = menu_bar.addMenu('Edit')
    # creating undo action
    undo_action = edit_menu.addAction('Undo')
    undo_action.setShortcut('Ctrl+Z')
    undo_action.triggered.connect(window.text_edit_field.undo)
    # creating redo action
    redo_action = edit_menu.addAction('Redo')
    redo_action.setShortcut('Ctrl+Y')
    redo_action.triggered.connect(window.text_edit_field.redo)
    edit_menu.addSeparator()
    # creating the copy action
    copy_action = edit_menu.addAction('Copy')
    copy_action.setShortcut('Ctrl+C')
    copy_action.triggered.connect(window.text_edit_field.copy)
    # creating the paste action
    paste_action = edit_menu.addAction('Paste')
    paste_action.setShortcut('Ctrl+V')
    paste_action.triggered.connect(window.text_edit_field.paste)
    # creating the cut action
    cut_action = edit_menu.addAction('Cut')
    cut_action.setShortcut('Ctrl+X')
    cut_action.triggered.connect(window.text_edit_field.cut)
    # creating the find action
    find_action = edit_menu.addAction('Find')
    find_action.setShortcut('Ctrl+F')
    find_action.triggered.connect(lambda: window.find_phrase(window))
    # creating the go to action
    go_to_action = edit_menu.addAction('Go to')
    go_to_action.setShortcut('Ctrl+G')
    go_to_action.triggered.connect(lambda: window.go_to_row(window))
    # creating the Search in Google action
    search_in_google_action = edit_menu.addAction('Search in Google')
    search_in_google_action.setShortcut('Ctrl+Shift+G')
    search_in_google_action.triggered.connect(window.google_search)
    edit_menu.addSeparator()
    # creating the clear action
    clear_all_action = edit_menu.addAction('Clear all')
    clear_all_action.setShortcut('Ctrl+DEL')
    clear_all_action.triggered.connect(window.text_edit_field.clear)
    # creating select all action
    select_all_action = edit_menu.addAction('Select all')
    select_all_action.setShortcut('Ctrl+A')
    select_all_action.triggered.connect(window.text_edit_field.selectAll)
    # creating date/time action to paste timestamp
    date_time_action = edit_menu.addAction('Date/Time')
    date_time_action.setShortcut('F5')
    date_time_action.triggered.connect(window.date_time)

    # creating the FORMAT menu on menubar
    format_menu = menu_bar.addMenu('Format')
    # creating font action
    font_action = format_menu.addAction('Font')
    font_action.triggered.connect(window.font_selection)
    # creating the WRAP TEXT action
    wrap_text_action = format_menu.addAction('Wrap text')
    wrap_text_action.setCheckable(True)
    wrap_text_action.triggered.connect(lambda: window.set_text_wrapping(wrap_text_action))

    # creating VIEW menu
    view_menu = menu_bar.addMenu('View')
    # creating zoom sub-menu
    zoom_submenu = view_menu.addMenu('Zoom')
    # creating zoom-in action, setting shortcut and adding to the submenu
    zoom_in_action = QAction('Zoom in', window)
    zoom_in_action.setShortcut('Ctrl++')
    zoom_in_action.triggered.connect(window.zoom_in)
    zoom_submenu.addAction(zoom_in_action)
    # creating zoom-out action, setting shortcut and adding to submenu
    zoom_out_action = QAction('Zoom out', window)
    zoom_out_action.setShortcut('Ctrl+-')
    zoom_out_action.triggered.connect(window.zoom_out)
    zoom_submenu.addAction(zoom_out_action)
    view_menu.addSeparator()
    # creating toolbar action
    toolbar_action = QAction('Toolbar', window)
    toolbar_action.setCheckable(True)
    toolbar_action.setChecked(True)
    toolbar_action.triggered.connect(lambda: window.tool_bar_display(toolbar_action))
    view_menu.addAction(toolbar_action)
