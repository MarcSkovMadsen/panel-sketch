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

COMPILERS = ["pyodide"]
DEFAULT_COMPILER = "pyodide"


class SketchBase(param.Parameterized):
    """SketchBase is the basic Data Model of a Sketch"""

    object = param.String(
        default=DEFAULT_SKETCH, doc="""A Python script. Is compiled to javascript and run."""
    )
    html = param.String(
        default="""<div id="sketch-holder"></div>""", doc="""A HTML String. Marksup the Sketch."""
    )
    css = param.String(default="", doc="""A CSS String. Styles the Sketch""")
    javascript = param.String(default="", doc="""The output from the compilation of python""")

    args = param.Dict(
        doc="""A Dictionary of keys and values that can be used in the python script"""
    )

    template = param.ObjectSelector(DEFAULT_TEMPLATE, objects=TEMPLATES)
    compiler = param.ObjectSelector(DEFAULT_COMPILER, objects=COMPILERS)

    def __init__(self, **params):
        if "args" not in params:
            params["args"] = {}

        super().__init__(**params)
