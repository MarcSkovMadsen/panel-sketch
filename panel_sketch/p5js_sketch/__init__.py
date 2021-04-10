import pathlib
import uuid

import panel as pn
import param

from ..sketch import Sketch

pn.config.js_files["p5"] = "https://cdnjs.cloudflare.com/ajax/libs/p5.js/1.3.1/p5.js"
pn.config.js_files["pyodide"] = "https://pyodide-cdn2.iodide.io/v0.15.0/full/pyodide.js"


ROOT = pathlib.Path(__file__).parent
TEMPLATE_PYODIDE_PATH = ROOT / "template_pyodide.js"
TEMPLATE_PYODIDE = TEMPLATE_PYODIDE_PATH.read_text()

DEFAULT_SKETCH = """
def setup():

    createCanvas(200, 200)

    background(160)

def draw():

    fill("blue")

    background(200)

    radius = sin(frameCount / 60) * 50 + 50

    ellipse(100, 100, radius, radius)
"""


class P5jsSketch(Sketch):
    object = param.String(DEFAULT_SKETCH)

    _template = TEMPLATE_PYODIDE

    def __init__(self, **params):
        params["args"] = params.get("args", {})

        super().__init__(**params)

        self._uuid = uuid.uuid4()

        self._html_pane = pn.pane.HTML(height=200, width=200)
        self._js_args_pane = pn.pane.HTML(width=0, height=0, margin=0, sizing_mode="fixed")
        self._js_pane = pn.pane.HTML(width=0, height=0, margin=0, sizing_mode="fixed")
        self.view = pn.Column(self._html_pane, self._js_args_pane, self._js_pane)

        self._update_html_pane()
        self._update_js_args_pane()
        self._update_js_pane()

    @param.depends("html", watch=True)
    def _update_html_pane(self):
        self._html_pane.object = self._compile_html()

    @param.depends("args", watch=True)
    def _update_js_args_pane(self):
        self._js_args_pane.object = self._compile_args()

    @param.depends("object", watch=True)
    def _update_js_pane(self):
        self._update_layout()

        self._js_pane.object = f"""<script type="module">{self._compile_object()}</script>"""

    def _update_layout(self):
        width, height, sizing_mode = self._get_layout(self.object)
        print(width, height, sizing_mode)
        if height:
            self._html_pane.height = height
        if width:
            self._html_pane.width = width
        if sizing_mode:
            self._html_pane.sizing_mode = sizing_mode

    def _compile_args(self):
        return f"""<script type="text/javascript">var args = {str(self.args)}</script>"""

    def _compile_html(self):
        return self.html.replace("sketch-holder", f"sketch-{self._uuid}")

    def _compile_object(self):
        object = self._clean_object(self.object)
        return self._template.replace("{{sketch-holder}}", f"sketch-{self._uuid}").replace(
            "{{sketch_object}}", object
        )
