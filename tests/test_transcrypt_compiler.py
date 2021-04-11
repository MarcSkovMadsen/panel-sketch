# pylint: disable=redefined-outer-name,protected-access
# pylint: disable=missing-function-docstring,missing-module-docstring,missing-class-docstring
from panel_sketch.sketch_compiler import SketchBase, TranscryptCompiler

SKETCH_PYTHON = """
print('Hello Compiler World')
"""


def duplicate_count(value):
    return len([x for x in set(value) if value.count(x) > 1])


def test_can_construct():
    sketch = SketchBase(object=SKETCH_PYTHON, template="basic")
    compiler = TranscryptCompiler(sketch=sketch)

    compiler.run()

    # When concatenating transcrypt generated modules we need to make sure they only appear once
    assert sketch.javascript.count("var __name__") == 1
    assert (
        sketch.javascript.count("var sketchElement = document.getElementById('sketch-element')\n")
        == 1
    )

def test_can_construct():
    sketch = SketchBase(object=SKETCH_PYTHON, template="pyp5js")
    compiler = TranscryptCompiler(sketch=sketch)

    compiler.run()

    # When concatenating transcrypt generated modules we need to make sure they only appear once
    assert sketch.javascript.count("var __name__") == 1
    assert sketch.javascript.count("var float") == 1
    assert (
        sketch.javascript.count("var sketchElement = document.getElementById('sketch-element')\n")
        == 1
    )
