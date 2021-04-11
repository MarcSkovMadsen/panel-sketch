import pathlib

import panel as pn
import param

from panel_sketch import Sketch

pn.config.sizing_mode = "stretch_width"
pn.extension("ace")

ROOT = pathlib.Path(__file__).parent
EXAMPLES = {
    "PyP5JS - Basic": "sketch_000.py",
    "PyP5JS - Angles and mouse coordinates": "sketch_001.py",
    "PyP5JS - Move Eye": "sketch_002.py",
    # "PyP5JS - Boids": "sketch_004.py", Does not work with pyodide
    "PyP5JS - Globals variables (HSB and CENTER)": "sketch_005.py",
    # "PyP5JS - Registering event functions such as keyPressed": "sketch_006.py",
    "PyP5JS - p5.Vector static methods": "sketch_007.py",
    "PyP5JS - p5.dom.js usage": "sketch_008.py",
    # "PyP5JS - Working with images": "sketch_008.py", # Need to serve assets
    "PyP5JS - Complex Shapes": "sketch_010.py",
}
EXAMPLE = list(EXAMPLES.keys())[0]


class Gallery(param.Parameterized):
    example = param.ObjectSelector(EXAMPLE, objects=list(EXAMPLES.keys()))
    sketch = param.ClassSelector(class_=Sketch)

    def __init__(self, **params):
        super().__init__(**params)

        self.sketch = Sketch()
        self._update_sketch_object()

    @param.depends("example", watch=True)
    def _update_sketch_object(self):
        self.sketch.html = self.sketch.param.html.default
        self.sketch.css = self.sketch.param.css.default
        self.sketch.object = (ROOT / EXAMPLES[self.example]).read_text()


pn.config.sizing_mode = "stretch_width"
gallery = Gallery()

template = pn.template.FastListTemplate(
    site="Panel Sketch", title="Examples", main_max_width="1200px"
)
template.sidebar[:] = [
    gallery.sketch.param.template,
    gallery.param.example,
    gallery.sketch.param.compiler,
]
template.main[:] = [
    pn.Column(
        pn.pane.Markdown("# ✏️ Sketch"),
        pn.layout.Divider(sizing_mode="stretch_width"),
        gallery.sketch.viewer.view,
    ),
    gallery.sketch.editor.view,
]

template.servable()
