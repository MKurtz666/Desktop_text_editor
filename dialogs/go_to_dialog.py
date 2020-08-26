from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtPrintSupport import *


class GoToDialog(QDialog):

    def __init__(self, parent):
        QDialog.__init__(self, parent)
        self.setParent(parent)
        self.setWindowTitle('Go to row')
        self.setFixedHeight(80)
        self.setWindowIcon(QIcon('://icon_go_to.png'))
        self.parent_text_field = parent.text_edit_field
        # defining the layout as grid layout
        goto_dialog_layout = QGridLayout()
        # creating the field for entering searched phrase
        self.row_input = QLineEdit()
        self.row_input.setValidator(QIntValidator(1, 999999))
        self.row_input.setFixedWidth(40)
        goto_dialog_layout.addWidget(self.row_input, 1, 2, 1, 2)
        # creating the find label
        row_num_label = QLabel('Row number:')
        goto_dialog_layout.addWidget(row_num_label, 1, 1, 1, 1)
        # creating the find next button
        go_to_button = QPushButton('Find next')
        # go_to_button.clicked.connect(self.go_to_row)
        goto_dialog_layout.addWidget(go_to_button, 2, 1, 1, 1)
        # creating the cancel button
        cancel_button = QPushButton('Cancel')
        cancel_button.clicked.connect(self.close)
        goto_dialog_layout.addWidget(cancel_button, 2, 2, 1, 1)
        # setting the previously described layout for the dialog
        self.setLayout(goto_dialog_layout)
        self.setStyleSheet(parent.style_sheet)
        self.show()