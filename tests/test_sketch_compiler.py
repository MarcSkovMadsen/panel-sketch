# pylint: disable=redefined-outer-name,protected-access
# pylint: disable=missing-function-docstring,missing-module-docstring,missing-class-docstring
from panel_sketch.sketch_compiler import PyodideCompiler, SketchBase

SKETCH_PYTHON = """
print('Hello Compiler World')
"""


def test_can_construct():
    # Given
    script = "print('Hello Compiler World')"
    sketch = SketchBase(object=script, template="pyp5js")
    compiler = PyodideCompiler(sketch=sketch)

    assert sketch.javascript == ""

    # When
    compiler.run()

    # Then
    assert script in sketch.javascript


def test_can_compile_basic_template():
    # Given
    script = "print('Hello Compiler World')"
    sketch = SketchBase(object=script, template="basic")
    compiler = PyodideCompiler(sketch=sketch)

    # When
    compiler.run()

    # Then
    assert "_P5_INSTANCE" not in sketch.javascript
