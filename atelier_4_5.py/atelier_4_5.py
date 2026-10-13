import random
from maya import cmds
from PySide6.QtWidgets import (
    QWidget,
    QPushButton,
    QVBoxLayout,
    QHBoxLayout,
    QLabel,
    QSpinBox,
    QDoubleSpinBox
)


class RandomGenerator(QWidget):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Atelier 4")
        self.setFixedWidth(260)

        self.build_ui()

    def build_ui(self):
        layout = QVBoxLayout(self)

        # Nombre d'objets
        ligne = QHBoxLayout()
        ligne.addWidget(QLabel("Number of objects"))

        self.nombre = QSpinBox()
        self.nombre.setRange(1, 1000)
        self.nombre.setValue(20)
        ligne.addWidget(self.nombre)

        layout.addLayout(ligne)

        # Titres Min et Max
        ligne = QHBoxLayout()
        ligne.addWidget(QLabel(""))
        ligne.addWidget(QLabel("Min"))
        ligne.addWidget(QLabel("Max"))
        layout.addLayout(ligne)

        # Positions X, Y et Z
        self.pos_min = {}
        self.pos_max = {}

        for axe in ["X", "Y", "Z"]:
            ligne = QHBoxLayout()
            ligne.addWidget(QLabel("Position " + axe))

            minimum = QDoubleSpinBox()
            minimum.setRange(-1000, 1000)
            minimum.setValue(-10)
            self.pos_min[axe] = minimum
            ligne.addWidget(minimum)

            maximum = QDoubleSpinBox()
            maximum.setRange(-1000, 1000)
            maximum.setValue(10)
            self.pos_max[axe] = maximum
            ligne.addWidget(maximum)

            layout.addLayout(ligne)

        # Échelle
        ligne = QHBoxLayout()
        ligne.addWidget(QLabel("Scale"))

        self.scale_min = QDoubleSpinBox()
        self.scale_min.setRange(0.1, 1000)
        self.scale_min.setValue(0.5)
        ligne.addWidget(self.scale_min)

        self.scale_max = QDoubleSpinBox()
        self.scale_max.setRange(0.1, 1000)
        self.scale_max.setValue(2)
        ligne.addWidget(self.scale_max)

        layout.addLayout(ligne)

        # Bouton
        self.create_button = QPushButton("Create objects")
        self.create_button.clicked.connect(self.create_object)
        layout.addWidget(self.create_button)

    def create_object(self):

        # Vérifier les valeurs
        for axe in ["X", "Y", "Z"]:
            if self.pos_min[axe].value() > self.pos_max[axe].value():
                cmds.warning("Min doit être inférieur à Max.")
                return

        if self.scale_min.value() > self.scale_max.value():
            cmds.warning("Scale Min doit être inférieur à Scale Max.")
            return

        # Créer les objets
        for i in range(self.nombre.value()):

            forme = random.choice(["cube", "cylindre", "sphere"])

            if forme == "cube":
                objet = cmds.polyCube()[0]

            elif forme == "cylindre":
                objet = cmds.polyCylinder()[0]

            else:
                objet = cmds.polySphere()[0]

            # Position aléatoire
            x = random.uniform(
                self.pos_min["X"].value(),
                self.pos_max["X"].value()
            )

            y = random.uniform(
                self.pos_min["Y"].value(),
                self.pos_max["Y"].value()
            )

            z = random.uniform(
                self.pos_min["Z"].value(),
                self.pos_max["Z"].value()
            )

            cmds.move(x, y, z, objet)

            # Échelle aléatoire
            scale = random.uniform(
                self.scale_min.value(),
                self.scale_max.value()
            )

            cmds.scale(scale, scale, scale, objet)


def main():
    global tool_window

    try:
        tool_window.close()
        tool_window.deleteLater()
    except:
        pass

    tool_window = RandomGenerator()
    tool_window.show()


main()