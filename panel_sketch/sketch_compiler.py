import param
from textwrap import dedent
import pathlib

from .sketch_base import SketchBase

ROOT = pathlib.Path(__file__).parent
TEMPLATE_PYODIDE_PATH = ROOT / "template_pyodide.js"
TEMPLATE_PYODIDE = TEMPLATE_PYODIDE_PATH.read_text()

PYODIDE_TEMPLATES = {
    "pyp5js": TEMPLATE_PYODIDE
}

class SketchCompilerBase(param.Parameterized):
    run = param.Action(constant=True)

    sketch = param.ClassSelector(class_=SketchBase, precedence=-1, constant=True)

    def __init__(self, **params):
        super().__init__(**params)

        with param.edit_constant(self):
            self.run = self._run_compiler

    def _run_compiler(self):
        self.sketch.javascript = self._compile(self.sketch.object, self.sketch.template)

    @classmethod
    def _compile(cls, sketch_object, template_value):
        raise NotImplementedError("Implement this is child classes")

class PyodideCompiler(SketchCompilerBase):
    run = param.Action(constant=True)

    sketch = param.ClassSelector(class_=SketchBase, precedence=-1, constant=True)

    def __init__(self, **params):
        super().__init__(**params)
        with param.edit_constant(self):
            self.name = "Pyodide"

    @classmethod
    def _compile(cls, sketch_object, template):
        sketch_object = cls._clean_object(sketch_object)
        template_string = PYODIDE_TEMPLATES[template]
        return template_string.replace("{{sketch_object}}", sketch_object)

    @staticmethod
    def _clean_object(value: str) -> str:
        clean = dedent(value)
        clean = clean.replace("from pyp5js import *\n", "")
        return clean

COMPILERS = {
    "pyodide": PyodideCompiler
}
