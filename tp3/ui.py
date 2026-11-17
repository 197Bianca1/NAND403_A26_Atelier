from PySide6 import QtWidgets


from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QPushButton, QLabel, QSpinBox, QDoubleSpinBox, QGroupBox



class RandoAnimatorUI(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()

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

        timing_group2 = QtWidgets.QGroupBox("translate parameters")
        timing_layout2 = QtWidgets.QHBoxLayout(timing_group2)

        self.translate_max_x = QtWidgets.QDoubleSpinBox()
        self.translate_max_x.setRange(0, 1000)
        self.translate_max_x.setValue(0)

        self.translate_max_y = QtWidgets.QDoubleSpinBox()
        self.translate_max_y.setRange(0, 1000)
        self.translate_max_y.setValue(0)

        self.translate_max_z = QtWidgets.QDoubleSpinBox()
        self.translate_max_z.setRange(0, 1000)
        self.translate_max_z.setValue(0)

        self.translate_min_x = QtWidgets.QDoubleSpinBox()
        self.translate_min_x.setRange(0, -1000)
        self.translate_min_x.setValue(0)

        self.translate_min_y = QtWidgets.QDoubleSpinBox()
        self.translate_min_y.setRange(0, -1000)
        self.translate_min_y.setValue(0)

        self.translate_min_z = QtWidgets.QDoubleSpinBox()
        self.translate_min_z.setRange(0, -1000)
        self.translate_min_z.setValue(0)

        timing_layout2.addWidget(
            QtWidgets.QLabel("min_x:")
        )
        timing_layout2.addWidget(self.translate_min_x)

        timing_layout2.addWidget(
            QtWidgets.QLabel("min_y:")
        )
        timing_layout2.addWidget(self.translate_min_y)

        timing_layout2.addWidget(
            QtWidgets.QLabel("min_z:")
        )
        timing_layout2.addWidget(self.translate_min_z)

        timing_layout2.addWidget(
            QtWidgets.QLabel("max_x:")
                )
        timing_layout2.addWidget(self.translate_max_x)
        
        timing_layout2.addWidget(
                    QtWidgets.QLabel("max_y:")
                )
        timing_layout2.addWidget(self.translate_max_y)
        
        timing_layout2.addWidget(
                    QtWidgets.QLabel("max_z:")
                )
        timing_layout2.addWidget(self.translate_max_z)

        layout.addWidget(timing_group2)

        rotation_group = QtWidgets.QGroupBox("rotation parameters")
        rotation_layout = QtWidgets.QHBoxLayout(rotation_group)

        self.rotation_max_x = QtWidgets.QDoubleSpinBox()
        self.rotation_max_x.setRange(0, 180)
        self.rotation_max_x.setValue(0)

        self.rotation_max_y = QtWidgets.QDoubleSpinBox()
        self.rotation_max_y.setRange(0, 180)
        self.rotation_max_y.setValue(0)

        self.rotation_max_z = QtWidgets.QDoubleSpinBox()
        self.rotation_max_z.setRange(0, 180)
        self.rotation_max_z.setValue(0)

        self.rotation_min_x = QtWidgets.QDoubleSpinBox()
        self.rotation_min_x.setRange(0, -180)
        self.rotation_min_x.setValue(0)
        
        self.rotation_min_y = QtWidgets.QDoubleSpinBox()
        self.rotation_min_y.setRange(0, -180)
        self.rotation_min_y.setValue(0)
        
        self.rotation_min_z = QtWidgets.QDoubleSpinBox()
        self.rotation_min_z.setRange(0, -180)
        self.rotation_min_z.setValue(0)

        rotation_layout.addWidget(
            QtWidgets.QLabel("min_x:")
        )
        rotation_layout.addWidget(self.rotation_min_x)

        rotation_layout.addWidget(
            QtWidgets.QLabel("min_y:")
        )
        rotation_layout.addWidget(self.rotation_min_y)

        rotation_layout.addWidget(
            QtWidgets.QLabel("min_z:")
        )
        rotation_layout.addWidget(self.rotation_min_z)

        rotation_layout.addWidget(
            QtWidgets.QLabel("max_x:")
        )
        rotation_layout.addWidget(self.rotation_max_x)

        rotation_layout.addWidget(
            QtWidgets.QLabel("max_y:")
            )
        rotation_layout.addWidget(self.rotation_max_y)
        
        rotation_layout.addWidget(
            QtWidgets.QLabel("max_z:")
            )
        rotation_layout.addWidget(self.rotation_max_z)

        layout.addWidget(rotation_group)

        scale_group = QtWidgets.QGroupBox("scale parameters")
        scale_layout = QtWidgets.QHBoxLayout(scale_group)

        self.scale_max_x = QtWidgets.QDoubleSpinBox()
        self.scale_max_x.setRange(0, 100)
        self.scale_max_x.setValue(1)

        self.scale_max_y = QtWidgets.QDoubleSpinBox()
        self.scale_max_y.setRange(0, 100)
        self.scale_max_y.setValue(1)

        self.scale_max_z = QtWidgets.QDoubleSpinBox()
        self.scale_max_z.setRange(0, 100)
        self.scale_max_z.setValue(1)

        self.scale_min_x = QtWidgets.QDoubleSpinBox()
        self.scale_min_x.setRange(0, -100)
        self.scale_min_x.setValue(1)
        
        self.scale_min_y = QtWidgets.QDoubleSpinBox()
        self.scale_min_y.setRange(0, -100)
        self.scale_min_y.setValue(1)
        
        self.scale_min_z = QtWidgets.QDoubleSpinBox()
        self.scale_min_z.setRange(0, -100)
        self.scale_min_z.setValue(1)

        scale_layout.addWidget(
            QtWidgets.QLabel("min_x:")
        )
        scale_layout.addWidget(self.scale_min_x)

        scale_layout.addWidget(
            QtWidgets.QLabel("min_y:")
        )
        scale_layout.addWidget(self.scale_min_y)

        scale_layout.addWidget(
            QtWidgets.QLabel("min_z:")
        )
        scale_layout.addWidget(self.scale_min_z)

        scale_layout.addWidget(
            QtWidgets.QLabel("max_x:")
        )
        scale_layout.addWidget(self.scale_max_x)

        scale_layout.addWidget(
            QtWidgets.QLabel("max_y:")
        )
        scale_layout.addWidget(self.scale_max_y)

        scale_layout.addWidget(
            QtWidgets.QLabel("max_z:")
        )
        scale_layout.addWidget(self.scale_max_z)

        layout.addWidget(scale_group)

        self.button = QtWidgets.QPushButton("Generate")
        self.button.setFixedSize(100,30)
       
        layout = QtWidgets.QHBoxLayout()
        layout.addStretch()
        layout.addWidget(self.button)
        layout.addLayout(button_layout)
        




        





        

        
