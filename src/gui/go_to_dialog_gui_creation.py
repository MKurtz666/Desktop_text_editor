from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *


def go_to_dialog_create_gui(window, parent):
    window.setParent(parent)
    window.setWindowTitle('Go to row')
    window.setFixedHeight(80)
    window.setWindowIcon(QIcon('://icon_go_to.png'))
    window.parent_text_field = parent.text_edit_field
    # defining the layout as grid layout
    goto_dialog_layout = QGridLayout()
    # creating the field for entering searched phrase
    window.row_input = QLineEdit()
    window.row_input.setValidator(QIntValidator(1, 999999))
    window.row_input.setFixedWidth(40)
    goto_dialog_layout.addWidget(window.row_input, 1, 2, 1, 2)
    # creating the find label
    row_num_label = QLabel('Row number:')
    goto_dialog_layout.addWidget(row_num_label, 1, 1, 1, 1)
    # creating the find next button
    go_to_button = QPushButton('Find next')
    # go_to_button.clicked.connect(window.go_to_row)
    goto_dialog_layout.addWidget(go_to_button, 2, 1, 1, 1)
    # creating the cancel button
    cancel_button = QPushButton('Cancel')
    cancel_button.clicked.connect(window.close)
    goto_dialog_layout.addWidget(cancel_button, 2, 2, 1, 1)
    # setting the previously described layout for the dialog
    window.setLayout(goto_dialog_layout)
    window.setStyleSheet(parent.style_sheet)
    window.show()
