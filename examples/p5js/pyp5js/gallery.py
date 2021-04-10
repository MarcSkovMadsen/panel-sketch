import pathlib

import panel as pn
import param

from panel_sketch.p5js_sketch import P5jsSketch
from panel_sketch.sketch import Sketch

pn.config.sizing_mode = "stretch_width"
# pn.config.css_files.append("https://cdnjs.cloudflare.com/ajax/libs/highlight.js/9.15.6/styles/default.min.css")
# pn.config.js_files["highlight"]="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/9.15.6/highlight.min.js"
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
    sketch = param.ClassSelector(class_=P5jsSketch)

    def __init__(self, **params):
        super().__init__(**params)

        self.sketch = P5jsSketch()
        self._update_sketch_object()

    @param.depends("example", watch=True)
    def _update_sketch_object(self):
        self.sketch.object = (ROOT / EXAMPLES[self.example]).read_text()


pn.config.sizing_mode = "stretch_width"
gallery = Gallery()

code_editor = pn.widgets.Ace(language="python", readonly=True, height=600)


@param.depends(code=gallery.sketch.param.object, watch=True)
def _update_code_editor(code):
    code_editor.value = code


_update_code_editor(gallery.sketch.object)

template = pn.template.FastListTemplate(site="Panel Sketch", title="P5js Examples")
template.sidebar[:] = [gallery.param.example]
template.main[:] = [gallery.sketch.view, code_editor]

template.servable()
