# pylint: disable=redefined-outer-name,protected-access
# pylint: disable=missing-function-docstring,missing-module-docstring,missing-class-docstring
from panel_sketch.sketch_viewer import SketchBase, SketchViewer


def test_can_constructor():
    sketch = SketchBase(javascript="console.log('sketch-element')")
    viewer = SketchViewer(sketch=sketch)

    assert viewer.sketch == sketch
    assert viewer.view

    assert "sketch-" in viewer._html_pane.object
    assert "sketch-" in viewer._js_pane.object

    assert "sketch-element" not in viewer._html_pane.object
    assert "sketch-element" not in viewer._js_pane.object


def test_get_layout_fixed():
    sketch = """
def setup():

    createCanvas(200, 200)

    background(160)
"""
    assert SketchViewer._get_layout(sketch) == (200, 200, "fixed")


def test_get_layout_none():
    sketch = """
def setup():

    background(160)
"""
    assert SketchViewer._get_layout(sketch) == (None, None, None)


def test_get_layout_more_args():
    sketch = """
    def setup():
        createCanvas(640, 360, _P5_INSTANCE.WEBGL)
        fill(204)
"""
    assert SketchViewer._get_layout(sketch) == (640, 360, "fixed")
