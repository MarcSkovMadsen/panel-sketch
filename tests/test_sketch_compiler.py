from panel_sketch.sketch_compiler import SketchCompilerBase, PyodideCompiler, SketchBase

SKETCH_PYTHON = """
print('Hello Compiler World')
"""

def test_can_construct():
    # Given
    script = "print('Hello Compiler World')"
    sketch=SketchBase(object=script, template="pyp5js")
    compiler = PyodideCompiler(sketch=sketch)

    assert sketch.javascript==""

    # When
    compiler.run()

    # Then
    assert script in sketch.javascript


