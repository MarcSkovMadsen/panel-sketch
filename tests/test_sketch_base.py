# pylint: disable=redefined-outer-name,protected-access
# pylint: disable=missing-function-docstring,missing-module-docstring,missing-class-docstring
from panel_sketch.sketch_base import SketchBase


def test_can_construct():
    sketch = SketchBase()

    assert sketch.args == {}
