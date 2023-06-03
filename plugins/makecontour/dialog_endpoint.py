from qtpy.QtCore import Signal, Qt, QCoreApplication, QMetaObject
from qtpy.QtWidgets import QDialog, QVBoxLayout, QFormLayout, QLabel, QLineEdit, QDoubleSpinBox, QDialogButtonBox
from yapsygui import Endpoint


class DialogEndpoint(QDialog):
    signalEndpoint = Signal(object)

    def __init__(self, parent):
        super().__init__(parent)
        self.setModal(True)
        self.endpoint = Endpoint()
        self.main_layout = QVBoxLayout(self)
        self.formLayout = QFormLayout()
        self.label_address = QLabel(self)
        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label_address)
        self.url = QLineEdit(self)
        self.url.setText("http://127.0.0.1")
        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.url)
        self.label_port = QLabel(self)
        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_port)
        self.port = QLineEdit(self)
        self.port.setText("5000")
        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.port)
        self.label_service = QLabel(self)
        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_service)
        self.service = QLineEdit(self)
        self.service.setText("zero_background")
        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.service)
        self.label_epsilon = QLabel(self)
        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.label_epsilon)
        self.doubleSpinBox = QDoubleSpinBox(self)
        self.doubleSpinBox.setDecimals(10)
        self.doubleSpinBox.setMaximum(0.9)
        self.doubleSpinBox.setSingleStep(0.0001)
        self.doubleSpinBox.setValue(0.0009)

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.doubleSpinBox)

        self.main_layout.addLayout(self.formLayout)

        self.buttonBox = QDialogButtonBox(self)
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel | QDialogButtonBox.Ok)

        self.main_layout.addWidget(self.buttonBox)

        self.retranslateUi(self)
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)

        QMetaObject.connectSlotsByName(self)

    def accept(self):
        self.endpoint.address = self.url.text()
        self.endpoint.port = self.port.text()
        self.endpoint.api = self.service.text()
        value = (self.doubleSpinBox.value(), self.endpoint)
        self.hide()
        self.signalEndpoint.emit(value)

    def reject(self):
        self.hide()

    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Endpoint", None))
        self.label_address.setText(QCoreApplication.translate("Dialog", u"Address", None))
        self.label_port.setText(QCoreApplication.translate("Dialog", u"Port", None))
        self.label_service.setText(QCoreApplication.translate("Dialog", u"Service", None))
        self.label_epsilon.setText(QCoreApplication.translate("Dialog", u"Epsilon", None))
    # retranslateUi
