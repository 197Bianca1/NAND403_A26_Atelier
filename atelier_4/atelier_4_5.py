import random
from maya import cmds
from PySide6.QtWidgets import (
    QWidget,
    QPushButton,
    QVBoxLayout,
    QLabel,
    QSpinBox,
    QDoubleSpinBox
)

class RandomGenerator(QWidget):
    
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Atelier 4-5")
        self.setMinimumWidth(400)
        self.build_ui()
    
    def build_ui(self):
        layout = QVBoxLayout(self)

        layout.addWidget(QLabel("ajouter forme"))

        self.nombre = QSpinBox()
        self.nombre.setRange(0,100)
        self.nombre.setSingleStep(5)
        self.nombre.setValue(0)

        layout.addWidget(QLabel("positin minimal"))

        self.pos_mini = QDoubleSpinBox()
        self.pos_mini.setRange(-100,100)
        self.pos_mini.setSingleStep(5)
        self.pos_mini.setValue(0)

        layout.addWidget(QLabel("position maximal"))

        self.pos_max = QDoubleSpinBox()
        self.pos_max.setRange(-100,100)
        self.pos_max.setSingleStep(1)
        self.pos_max.setValue(0)

        layout.addWidget(QLabel("taille minimal"))

        self.size_min = QDoubleSpinBox()
        self.size_min.setRange(0,100)
        self.size_min.setSingleStep(1)
        self.size_min.setValue(1)

        layout.addWidget(QLabel("taille maximum"))

        self.size_max = QDoubleSpinBox()
        self.size_max.setRange(0,100)
        self.size_max.setSingleStep(1)
        self.size_max.setValue(5)

        self.create_button = QPushButton("Create")
        self.create_button.clicked.connect(self.create_object)
        layout.addWidget(self.create_button)

    def create_object(self):

        if self.pos_mini.value() > self.pos_max.value():
            cmds.warning("La position minimale doit être inférieure à la position maximale.")
            return

        if self.size_min.value() > self.size_max.value():
            cmds.warning("La taille minimale doit être inférieure à la taille maximale.")
            return

        for i in range(self.nombre.value()):

            forme = random.choice(["cube", "cylindre", "sphere"])

            if forme == "cube":
                objet = cmds.polyCube()[0]
            elif forme == "cylindre":
                objet = cmds.polyCylinder()[0]
            else:
                objet = cmds.polySphere()[0]

            x = random.uniform(self.pos_mini.value(), self.pos_max.value())
            y = random.uniform(self.pos_mini.value(), self.pos_max.value())
            z = random.uniform(self.pos_mini.value(), self.pos_max.value())

            cmds.move(x, y, z, objet)

            scale = random.uniform(self.size_min.value(), self.size_max.value())
            cmds.scale(scale, scale, scale, objet)

def main():
    global tool_window
    try:
        tool_window.close()
    except Exception:
        pass
    tool_window = RandomGenerator()
    tool_window.show()

main()
