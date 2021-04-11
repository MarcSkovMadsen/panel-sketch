# pylint: disable=redefined-outer-name,protected-access
# pylint: disable=missing-function-docstring,missing-module-docstring,missing-class-docstring
from panel_sketch.sketch_editor import SketchBase, SketchEditor


def test_can_construct():
    sketch = SketchBase()
    editor = SketchEditor(sketch=sketch)

    assert editor.sketch is sketch
    assert editor.view


def test_can_update_sketch():
    sketch = SketchBase()
    editor = SketchEditor(sketch=sketch)

    sketch.object = "a"
    assert editor._python_editor.value == sketch.object

    sketch.html = "b"
    assert editor._html_editor.value == sketch.html

    sketch.css = "c"
    assert editor._css_editor.value == sketch.css

    sketch.javascript = "d"
    assert editor._javascript_editor.value == sketch.javascript


def test_can_compile():
    # Given
    sketch = SketchBase()
    editor = SketchEditor(sketch=sketch)

    assert editor._log.value == ""
    # When
    editor._python_editor.value = "print('a')"
    editor._html_editor.value = "<div id='sketch-element'></div>HI"
    editor._css_editor.value = """
#sketch-element {
    color: blue;
}
    """

    editor.compile()

    # Then
    assert sketch.object == editor._python_editor.value
    assert sketch.html == editor._html_editor.value
    assert sketch.css == editor._css_editor.value
