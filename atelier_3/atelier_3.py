from PySide6.QtWidgets import QWidget
 
class MessageBoard(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Message board")
 
def main():
    global widget
    try:
        widget.close()
    except Exception:
        pass
    widget = MessageBoard()
    widget.show()
 
main()