style_sheet_graphite = """

QMenuBar {
            spacing: 2px;
            background-color: #7c8e9c;
}

QMenuBar::item {   
            background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:3, stop:0 #7c8e9c, stop:1 000066);         
            padding: 5px 25px;
            color: #e2e6e9;            
}

QMenuBar::item::selected {
            background-color: #d3d9de;
            color: #161a1d;
}

QMenu {   
        background-color: #7c8e9c;   
}

QMenu::item {                         
            color: #e2e6e9;
}

QMenu::item::selected {
        background-color: #d3d9de;
        color: #161a1d;
}

QToolBar { 
        padding: 4px 5px;
        spacing: 10px;
        background-color: #7c8e9c;   
}

QToolButton {        
        background-color: #7c8e9c;
        color: #e2e6e9;                  
}

QMessageBox {        
        background-color: #7c8e9c;
}

QMessageBox QLabel {
        color: #e2e6e9;
}

QMessageBox QPushButton {         
        background-color: #7c8e9c;
        color: #e2e6e9;
}

QDialog {
        background-color: #7c8e9c;        
}

QDialog QPushButton {         
        background-color: #7c8e9c;
        color: #e2e6e9;
}

QDialog QLabel{
        color: #e2e6e9;
}

QPlainTextEdit {
        background-color: #12273b;
        selection-background-color: #92a8d1;
        color: #e6e2d3;
}

QStatusBar QLineEdit {
        color: #e2e6e9; 
        border: none; 
        background-color: #7c8e9c; 
        border-radius: 2px;
}

"""

style_sheet_sandstorm = """

QMenuBar {
            spacing: 2px;
            background-color: #ffe0b3;
}

QMenuBar::item {   
            background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:3, stop:0 #ffe0b3, stop:1 000066);         
            padding: 5px 25px;
            color: #1a0f00;            
}

QMenuBar::item::selected {
            background-color: #663c00;
            color: #ffeacc;
}

QMenu {   
        background-color: #ffe0b3;   
}

QMenu::item {                         
            color: #1a0f00;
}

QMenu::item::selected {
        background-color: #663c00;
        color: #ffeacc;
}

QToolBar { 
        padding: 4px 5px;
        spacing: 10px;
        background-color: #ffe0b3;   
}

QToolButton {        
        background-color: #ffe0b3;
        color: #1a0f00;                  
}

QMessageBox {        
        background-color: #ffe0b3;
}

QMessageBox QLabel {
        color: #1a0f00;
}

QMessageBox QPushButton {         
        background-color: #ffe0b3;
        color: #1a0f00;
}

QDialog {
        background-color: #ffe0b3;        
}

QDialog QPushButton {         
        background-color: #ffe0b3;
        color: #1a0f00;
}

QDialog QLabel{
        color: #1a0f00;
}

QPlainTextEdit {
        background-color: #1a0d00;
        selection-background-color: #00b300;
        color: #ffe6cc;
}

QStatusBar QLineEdit {
        color: #1a0f00; 
        border: none; 
        background-color: #ffe0b3; 
        border-radius: 2px;
}

"""

