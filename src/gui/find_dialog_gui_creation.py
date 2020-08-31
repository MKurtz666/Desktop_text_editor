from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *


def find_dialog_create_gui(window, parent):
    window.setParent(parent)
    window.setWindowTitle('Find phrase')
    window.setFixedHeight(80)
    window.setWindowIcon(QIcon('://icon_find.png'))
    window.searched_text = None
    window.parent_text_field = parent.text_edit_field
    # defining the layout as grid layout
    find_dialog_layout = QGridLayout()
    # creating the field for entering searched phrase
    window.searched_phrase_input = QLineEdit()
    window.searched_phrase_input.setPlaceholderText('Enter searched phrase')
    find_dialog_layout.addWidget(window.searched_phrase_input, 1, 2, 1, 2)
    # creating the find label
    find_label = QLabel('Find:')
    find_dialog_layout.addWidget(find_label, 1, 1, 1, 1)
    # creating the find next button
    find_next_button = QPushButton('Find next')
    find_next_button.clicked.connect(lambda: window.search_for_text('F'))
    find_dialog_layout.addWidget(find_next_button, 2, 1, 1, 1)
    # creating the find previous button
    find_previous_button = QPushButton('Find previous')
    find_previous_button.clicked.connect(lambda: window.search_for_text('B'))
    find_dialog_layout.addWidget(find_previous_button, 2, 2, 1, 1)
    # creating the cancel button
    cancel_button = QPushButton('Cancel')
    cancel_button.clicked.connect(window.close)
    find_dialog_layout.addWidget(cancel_button, 2, 3, 1, 1)
    # setting the previously described layout for the dialog
    window.setLayout(find_dialog_layout)
    # setting the style sheet for dialog - same as parent widget
    window.setStyleSheet(parent.style_sheet)
    window.show()
