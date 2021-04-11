"""The Sketch Compilers makes it easy to compiles a Sketch"""
import pathlib
from textwrap import dedent
from typing import Dict

import param

from ..sketch_base import SketchBase

ROOT = pathlib.Path(__file__).parent

PYODIDE_TEMPLATE_STRINGS = {
    "basic": (ROOT / "template_pyodide_basic.js").read_text(),
    "pyp5js": (ROOT / "template_pyodide_pyp5js.js").read_text(),
}


class SketchCompilerBase(param.Parameterized):
    """The SketchCompilerBase should be inherited by child classes"""

    run = param.Action(constant=True)

    sketch = param.ClassSelector(class_=SketchBase, precedence=-1, constant=True)

    _TEMPLATE_STRINGS: Dict[str, str] = {}

    def __init__(self, **params):
        super().__init__(**params)

        with param.edit_constant(self):
            self.run = self._run_compiler

    def _run_compiler(self):
        # pylint: disable=no-member
        self.sketch.javascript = self._compile(self.sketch.object, self._template_string)

    @classmethod
    def _compile(cls, sketch_object, template_string):
        raise NotImplementedError("Implement this is child classes")

    @property
    def _template_string(self):
        # pylint: disable=no-member
        return self._TEMPLATE_STRINGS[self.sketch.template]


class PyodideCompiler(SketchCompilerBase):
    """The PyodideCompiler uses the Pyodide JS library"""

    run = param.Action(constant=True)

    sketch = param.ClassSelector(class_=SketchBase, precedence=-1, constant=True)

    _TEMPLATE_STRINGS: Dict[str, str] = PYODIDE_TEMPLATE_STRINGS

    def __init__(self, **params):
        super().__init__(**params)
        with param.edit_constant(self):
            self.name = "Pyodide"

    @classmethod
    def _compile(cls, sketch_object, template_string):
        sketch_object = cls._clean_object(sketch_object)
        return template_string.replace("{{sketch_object}}", sketch_object)

    @staticmethod
    def _clean_object(value: str) -> str:
        clean = dedent(value)
        clean = clean.replace("from pyp5js import *\n", "")
        return clean


COMPILERS = {"pyodide": PyodideCompiler}
