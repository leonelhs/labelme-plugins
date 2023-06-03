from qtpy.QtGui import QColor
from qtpy.QtWidgets import QVBoxLayout, QDialog
from pyqtspinner import WaitingSpinner


class DialogLoading(QDialog):
    def __init__(self, parent):
        super().__init__(parent)
        self.setModal(True)
        self.main_layout = QVBoxLayout(self)
        spinner = WaitingSpinner(
            self,
            roundness=100.0,
            fade=54,
            radius=30,
            lines=7,
            line_length=30,
            line_width=30,
            speed=0.8,
            color=QColor(97, 53, 131)
        )
        self.main_layout.addWidget(spinner)
        self.setLayout(self.main_layout)
        spinner.start()
