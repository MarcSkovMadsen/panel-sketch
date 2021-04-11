# pylint: disable=redefined-outer-name,protected-access
# pylint: disable=missing-function-docstring,missing-module-docstring,missing-class-docstring
from panel_sketch.sketch_compiler import PyodideCompiler

INDENTED = """
    def setup():
        pass

    def draw():
        pass
"""

UNINDENTED = """
def setup():
    pass

def draw():
    pass
"""


def test_clean_unindents():
    assert PyodideCompiler._clean_object(INDENTED) == UNINDENTED


def test_clean_removes_pyp5js_import():
    sketch = """
# https://p5js.org/examples/interaction-wavemaker.html


from pyp5js import *

t = 0
"""
    assert (
        PyodideCompiler._clean_object(sketch)
        == """
# https://p5js.org/examples/interaction-wavemaker.html



t = 0
"""
    )
