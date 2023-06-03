from yapsygui import APlugin


class DemoPlugin(APlugin):

    def __init__(self):
        text = "Demo plugin"
        icon = "tool.png"
        shortcut = ""
        tip = "Demo plugin"
        super().__init__(__file__, text, icon, shortcut, tip)

    def slot(self, context):
        points = [
            [139.22651933701658, 165.19337016574582],
            [139.22651933701658, 303.1933701657458],
            [439.22651933701655, 303.1933701657458],
            [439.22651933701655, 165.19337016574582]
        ]
        label = "box"
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

        context.loadLabels(shapes)
