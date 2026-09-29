from PySide6.QtWidgets import QWidget, QLabel, QVBoxLayout,QTextEdit, QPushButton, QMessageBox
 
class MessageBoard(QWidget):
    def __init__(self): # Constructeur
        super().__init__() # Constructeur QWidget
        self.setWindowTitle("Message board")
        self.create_ui()
 
    def create_ui(self):
        layout = QVBoxLayout(self)
        label = QLabel("Message board")
        layout.addWidget(label)

 
        # QTextEdit
        self.text_edit = QTextEdit()
        self.text_edit.setPlaceholderText("message")
        layout.addWidget(self.text_edit)
        
 
        # QPushButton
        button = QPushButton("Appuier")
        layout.addWidget(button)
        button.clicked.connect(self.on_click)
   
    def on_click(self):
        print("on click called")
        # QMessageBox
        message = self.text_edit.toPlainText()
        box = QMessageBox()
        box.setWindowTitle("message")
        box.setText(message)
        box.exec()
   
 
def main():
    global widget
    try:
        widget.close()
    except Exception:
        pass
    widget = MessageBoard()
    widget.show()
 
main()