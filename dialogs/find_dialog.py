from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from gui.find_dialog_gui_creation import find_dialog_create_gui


class FindDialog(QDialog):

    def __init__(self, parent):
        # adding the 'parent' arg to the init func to establish the relationship
        QDialog.__init__(self, parent)

        find_dialog_create_gui(self, parent)

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
