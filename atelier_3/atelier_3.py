from PySide6.QtWidgets import QWidget, QLabel, QVBoxLayout,QTextEdit, QPushButton
 
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
        text_edit = QTextEdit()
        text_edit.setPlaceholderText("message")
        layout.addWidget(text_edit)
        
 
        # QPushButton
        button = QPushButton("apuier")
        layout.addWidget(button)
   
    def on_click(self):
        print("on click called")
        # QMessageBox
   
 
def main():
    global widget
    try:
        widget.close()
    except Exception:
        pass
    widget = MessageBoard()
    widget.show()
 
main()