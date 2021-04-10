from panel_sketch.sketch import Sketch

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
    assert Sketch._clean_object(INDENTED) == UNINDENTED


def test_clean_removes_pyp5js_import():
    sketch = """
# https://p5js.org/examples/interaction-wavemaker.html


from pyp5js import *

t = 0
"""
    assert (
        Sketch._clean_object(sketch)
        == """
# https://p5js.org/examples/interaction-wavemaker.html



t = 0
"""
    )


def test_get_layout_fixed():
    sketch = """
def setup():

    createCanvas(200, 200)

    background(160)
"""
    assert Sketch._get_layout(sketch) == (200, 200, "fixed")


def test_get_layout_none():
    sketch = """
def setup():

    background(160)
"""
    assert Sketch._get_layout(sketch) == (None, None, None)


def test_get_layout_more_args():
    sketch = """
    def setup():
        createCanvas(640, 360, _P5_INSTANCE.WEBGL)
        fill(204)
"""
    assert Sketch._get_layout(sketch) == (640, 360, "fixed")
