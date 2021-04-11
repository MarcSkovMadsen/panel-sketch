"""The SketchViewer makes it easy to View a Sketch"""
import uuid
from textwrap import dedent

import panel as pn
import param

from .sketch_base import SketchBase

LAYOUT_NONE = (None, None, None)


class SketchViewer(param.Parameterized):
    """The SketchViewer makes it easy to View a Sketch"""
    sketch = param.ClassSelector(class_=SketchBase, constant=True, precedence=-1)

    view = param.Parameter(constant=True)


    def __init__(self, **params):
        super().__init__(**params)

        self._uuid = uuid.uuid4()
        self._create_view()

        self._update_html_pane()
        self._update_css_pane()
        self._update_js_args_pane()
        self._update_js_pane()

    def _create_view(self):
        self._html_pane = pn.pane.HTML(height=200, width=200)
        self._css_pane = pn.pane.HTML(width=0, height=0, margin=0, sizing_mode="fixed")
        self._js_args_pane = pn.pane.HTML(width=0, height=0, margin=0, sizing_mode="fixed")
        self._js_pane = pn.pane.HTML(width=0, height=0, margin=0, sizing_mode="fixed")
        with param.edit_constant(self):
            self.view = pn.Column(self._css_pane, self._html_pane, self._js_args_pane, self._js_pane)

    def _to_unique(self, value):
        return value.replace("sketch-holder", f"sketch-{self._uuid}")

    # pylint: disable=no-member
    @param.depends("sketch.html", watch=True)
    def _update_html_pane(self):
        html_unique = self._to_unique(self.sketch.html)
        self._html_pane.object = html_unique

    @param.depends("sketch.css", watch=True)
    def _update_css_pane(self):
        css_unique = self._to_unique(self.sketch.css)
        self._css_pane.object = "<style>" + css_unique + "</style>"

    @param.depends("sketch.args", watch=True)
    def _update_js_args_pane(self):
        javascript_args_unique = self._to_unique(f"""var args = {str(self.sketch.args)}""")
        self._js_args_pane.object = (
            f'<script type="text/javascript">{javascript_args_unique}</script>'
        )

    @param.depends("sketch.javascript", watch=True)
    def _update_js_pane(self):
        self._update_layout()
        javascript_unique = self._to_unique(self.sketch.javascript)
        self._js_pane.object = f"""<script type="module">{javascript_unique}</script>"""

    def _update_layout(self):
        width, height, sizing_mode = self._get_layout(self.sketch.object)
        if height:
            self._html_pane.height = height
        if width:
            self._html_pane.width = width
        if sizing_mode:
            self._html_pane.sizing_mode = sizing_mode

    @staticmethod
    def _get_layout(value: str):
        clean = dedent(value)
        index = clean.find("createCanvas(")  # '...createCanvas(200, 200)\n\n    background(160)'
        if index == -1:
            return LAYOUT_NONE

        clean = clean[index:-1].replace("createCanvas(", "")  # '200, 200)\n\n    background(160)'
        index = clean.find(")")
        clean = clean[0:index]  # '200, 200
        args = clean.split(",")
        width = int(args[0])
        height = int(args[1])
        sizing_mode = "fixed"
        return width, height, sizing_mode
