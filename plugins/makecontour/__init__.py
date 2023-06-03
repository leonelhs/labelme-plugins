import numpy as np
from qtpy.QtWidgets import QMainWindow
from yapsygui import NAPlugin

from .dialog_endpoint import DialogEndpoint
from .dialog_loading import DialogLoading
from .utils import findContours


class MakeContour(NAPlugin):

    def __init__(self):
        self.epsilon = None
        text = "Make contour"
        icon = "tool.png"
        shortcut = ""
        tip = "Make IA contour"
        super().__init__(__file__, text, icon, shortcut, tip)
        self.dialogLoading = DialogLoading(self.context)
        self.dialogEndpoint = DialogEndpoint(self.context)
        self.dialogEndpoint.signalEndpoint.connect(self.signalEndpointHandler)

    # @QtCore.Slot()
    def signalEndpointHandler(self, value):
        self.epsilon, endpoint = value
        self.dialogLoading.show()
        try:
            self.runRemoteTask(self.context.imageData, endpoint)
        except AttributeError:
            self.dialogLoading.hide()
            self.context.errorMessage("Shapes", "There is no open picture")

    def slot(self, context: QMainWindow):
        self.dialogEndpoint.show()

    def onRequestResponse(self, reply, api):
        self.dialogLoading.hide()
        image_mask = np.asarray(reply, dtype=np.uint8)
        points = findContours(image_mask, self.epsilon)
        self.drawShapes(points)

    def onRequestProgress(self, sent, total):
        self.context.statusBar().showMessage(str("sending %d of total %d") % (sent, total))
        self.context.statusBar().show()

    def onRequestError(self, message, error):
        self.dialogLoading.hide()
        self.context.errorMessage(str(error), str(message))

    def drawShapes(self, points):
        label = "body"
        shapes = [
            dict(
                label=label,
                group_id=None,
                points=points,
                shape_type="polygon",
                flags={},
                other_data={},
            )
        ]
        self.context.loadLabels(shapes)
