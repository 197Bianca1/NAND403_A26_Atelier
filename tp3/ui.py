from maya import cmds
from PySide6.QtWidgets import (
    QWidget,
    QPushButton,
    QVBoxLayout,
    QHBoxLayout,
    QLabel,
    QSpinBox,
    QDoubleSpinBox,
    QGroupBox,
    QHBoxLayout
)

from PySide6.QtWidgets import  QtCore

from animator import RandomAnimator



class RandoAnimatorUI(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Random Animation")
        self.setFixedWidth(500)

        self.animator = RandomAnimator()

        self.build_ui()

    def build_ui(self):

        layout = QtWidgets.QVBoxLayout(self)
        layout.setContentsMargins(8, 8, 8, 8)
        layout.setSpacing(4)

        timing_group = QtWidgets.QGroupBox("Animation Timing")
        timing_layout = QtWidgets.QHBoxLayout(timing_group)

        self.duration = QtWidgets.QSpinBox()
        self.duration.setRange(1, 10000)
        self.duration.setValue(100)

        self.interval = QtWidgets.QSpinBox()
        self.interval.setRange(1, 1000)
        self.interval.setValue(30)

        timing_layout.addWidget(
            QtWidgets.QLabel("Duration (Frames):")
        )
        timing_layout.addWidget(self.duration)

        timing_layout.addWidget(
            QtWidgets.QLabel("Step (Frames):")
        )
        timing_layout.addWidget(self.interval)

        layout.addWidget(timing_group)

        

        
