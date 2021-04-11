"""Sketch makes it easy for Pythonistas to quickly sketch interactive visualizations and other
applications running in.

- the browser. Potentially without a Python backend
- the Jupyter Notebook.
- your favorite editor or IDE.

It is heavily inspired by [p5js](https://p5js.org/get-started/),
[p5js sketches](https://editor.p5js.org/p5/sketches) and
[pyp5js](https://github.com/berinhard/pyp5js) but not limited to the p5js universe. You can also
think of it as a [Code Sandbox](https://codesandbox.io/) or
[JS Fiddle](https://jsfiddle.net/) but for #Python &#128013; and data science.
"""
import pathlib
from textwrap import dedent

import panel as pn
import param

from .sketch_base import SketchBase
from .sketch_editor import SketchEditor
from .sketch_viewer import SketchViewer
from .sketch_compiler import COMPILERS

pn.config.js_files["p5"] = "https://cdnjs.cloudflare.com/ajax/libs/p5.js/1.3.1/p5.js"
pn.config.js_files["pyodide"] = "https://pyodide-cdn2.iodide.io/v0.15.0/full/pyodide.js"


class Sketch(SketchBase):  # pylint: disable=too-many-instance-attributes
    """Sketch makes it easy for Pythonistas to quickly sketch interactive visualizations and other
    applications running in.

    - the browser. Potentially without a Python backend
    - the Jupyter Notebook.
    - your favorite editor or IDE.

    It is heavily inspired by [p5js](https://p5js.org/get-started/),
    [p5js sketches](https://editor.p5js.org/p5/sketches) and
    [pyp5js](https://github.com/berinhard/pyp5js) but not limited to the p5js universe. You can also
    think of it as a [Code Sandbox](https://codesandbox.io/) or
    [JS Fiddle](https://jsfiddle.net/) but for #Python &#128013; and data science."""

    def __init__(self, **params):
        params["args"] = params.get("args", {})

        super().__init__(**params)

        self._viewer = None
        self._editor = None
        self._compilers = {}

        self._compile_object()

    @property
    def viewer(self):
        """A Viewer that makes viewing the Sketch a joy"""
        if not self._viewer:
            self._viewer = SketchViewer(sketch=self)
        return self._viewer

    @property
    def editor(self):
        """An Editor that makes editing the Sketch a joy"""
        if not self._editor:
            self._editor = SketchEditor(sketch=self)
        return self._editor

    @property
    def _compiler(self):
        """The Compiler that makes compiling the Sketch a joy"""
        if not self.compiler in self._compilers:
            self._compilers[self.compiler] = COMPILERS[self.compiler](sketch=self)
        return self._compilers[self.compiler]

    @param.depends("object", watch=True)
    def _compile_object(self):
        self._compiler.run()
