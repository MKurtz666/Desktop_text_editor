from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from src.dialogs.TextEditMainWindow import TextEditMainWindow
import time

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
