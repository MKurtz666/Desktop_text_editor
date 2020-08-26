from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *


class FindDialog(QDialog):

    def __init__(self, parent):
        # adding the 'parent' arg to the init func to establish the relationship
        QDialog.__init__(self, parent)

        self.setParent(parent)
        self.setWindowTitle('Find phrase')
        self.setFixedHeight(80)
        self.setWindowIcon(QIcon('://icon_find.png'))
        self.searched_text = None
        self.parent_text_field = parent.text_edit_field
        # defining the layout as grid layout
        find_dialog_layout = QGridLayout()
        # creating the field for entering searched phrase
        self.searched_phrase_input = QLineEdit()
        self.searched_phrase_input.setPlaceholderText('Enter searched phrase')
        find_dialog_layout.addWidget(self.searched_phrase_input, 1, 2, 1, 2)
        # creating the find label
        find_label = QLabel('Find:')
        find_dialog_layout.addWidget(find_label, 1, 1, 1, 1)
        # creating the find next button
        find_next_button = QPushButton('Find next')
        find_next_button.clicked.connect(lambda: self.search_for_text('F'))
        find_dialog_layout.addWidget(find_next_button, 2, 1, 1, 1)
        # creating the find previous button
        find_previous_button = QPushButton('Find previous')
        find_previous_button.clicked.connect(lambda: self.search_for_text('B'))
        find_dialog_layout.addWidget(find_previous_button, 2, 2, 1, 1)
        # creating the cancel button
        cancel_button = QPushButton('Cancel')
        cancel_button.clicked.connect(self.close)
        find_dialog_layout.addWidget(cancel_button, 2, 3, 1, 1)
        # setting the previously described layout for the dialog
        self.setLayout(find_dialog_layout)
        # setting the style sheet for dialog - same as parent widget
        self.setStyleSheet(parent.style_sheet)
        self.show()

    def search_for_text(self, direction):
        # attribute storing the phrase that we're looking for
        self.searched_text = self.searched_phrase_input.text()
        # running find() built in on the text field of the parent widget
        if direction == 'F':
            self.parent_text_field.find(self.searched_text)
        else:
            self.parent_text_field.find(self.searched_text, QTextDocument.FindBackward)
        # if phrase not in parent text field show popup message
        if self.searched_text not in self.parent_text_field.toPlainText() \
                and self.searched_text.capitalize() not in self.parent_text_field.toPlainText() \
                and self.searched_text.lower() not in self.parent_text_field.toPlainText() \
                and self.searched_text.upper() not in self.parent_text_field.toPlainText():
            not_found_popup = QMessageBox.information(self, 'Not found', 'Phrase not found', QMessageBox.Ok)