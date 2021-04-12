"""SketchBase is the basic Data Model of a Sketch"""
import param

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

TEMPLATES = ["basic", "pyp5js"]
DEFAULT_TEMPLATE = "pyp5js"

COMPILERS = ["pyodide", "transcrypt"]
DEFAULT_COMPILER = "pyodide"


class SketchBase(param.Parameterized):
    """SketchBase is the basic Data Model of a Sketch"""

    object = param.String(
        default=DEFAULT_SKETCH,
        doc="""A Python script. It is transpiled to javascript (Transcript) or run directly in javascript (Pyodide). You can reference the `div` element via `sketchElement` in Python""",
    )
    html = param.String(
        default="""<div id="sketch-element"></div>""",
        doc="""A HTML String to mark up the Sketch.""",
    )
    css = param.String(
        default="",
        doc="""A CSS String to style the Sketch. You can style the HTML div via the `#sketch-element` reference.""",
    )
    javascript = param.String(
        default="", doc="""The result of the compilation of the python object."""
    )

    args = param.Dict(
        doc="""A Dictionary of keys and values that can be reference via `window.args` in the python script."""
    )

    template = param.ObjectSelector(
        DEFAULT_TEMPLATE,
        objects=TEMPLATES,
        doc="""The template to use for compilation. One of 'basic', 'pyp5js'. Default is (currently) 'pyp5js'.""",
    )
    compiler = param.ObjectSelector(DEFAULT_COMPILER, objects=COMPILERS)

    loading = param.Boolean(
        doc="""Whether or not the Sketch is loading. For example during compilation."""
    )

    def __init__(self, **params):
        if "args" not in params:
            params["args"] = {}

        super().__init__(**params)
