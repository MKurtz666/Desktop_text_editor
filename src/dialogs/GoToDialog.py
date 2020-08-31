from PyQt5.QtWidgets import *
from src.gui.go_to_dialog_gui_creation import go_to_dialog_create_gui


class GoToDialog(QDialog):

    def __init__(self, parent):
        QDialog.__init__(self, parent)

        go_to_dialog_create_gui(self, parent)

    def go_to_row(self):
        pass  # to be written
