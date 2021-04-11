"""The Sketch Compilers makes it easy to compiles a Sketch"""
import pathlib
import subprocess
import tempfile
from textwrap import dedent
from typing import Dict, List

import param

from ..sketch_base import SketchBase

ROOT = pathlib.Path(__file__).parent

PYODIDE_TEMPLATE_STRINGS = {
    "basic": (ROOT / "template_pyodide_basic.js").read_text(),
    "pyp5js": (ROOT / "template_pyodide_pyp5js.js").read_text(),
}

TRANSCRYPT_TEMPLATE_STRINGS = {
    "basic": (ROOT / "template_transcrypt_basic.py").read_text(),
    "pyp5js": (ROOT / "template_transcrypt_pyp5js.py").read_text(),
}

OBJECT_PREFIX = "sketchElement = document.getElementById('sketch-element')\n"

TRANSCRYPT_DIR = str(ROOT / "assets" / "js" / "transcrypt").replace("\\", "/") + "/"

print(f"""
    Remember to add --static-dirs transcrypt={TRANSCRYPT_DIR}"""
)


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
        python = OBJECT_PREFIX + self.sketch.object
        self.sketch.javascript = self._compile(python, self._template_string)

    @classmethod
    def _compile(cls, sketch_object, template_string):
        raise NotImplementedError("Implement this is child classes")

    @property
    def _template_string(self):
        # pylint: disable=no-member
        return self._TEMPLATE_STRINGS[self.sketch.template]


class TranscryptCompiler(SketchCompilerBase):
    """The TranscryptCompiler uses the Transcrypt Python library"""

    arguments = param.List(
        default=["transcrypt", "-b", "-n", "-m"],
        constant=True,
        doc="""The arguments to transpile from sketch.py to sketch.js""",
    )

    _TEMPLATE_STRINGS: Dict[str, str] = TRANSCRYPT_TEMPLATE_STRINGS

    @classmethod
    def _compile(cls, sketch_object, template_string):
        if "from pyp5js import *" in template_string:
            template_name = "pyp5js"
        else:
            template_name = "basic"
        with tempfile.TemporaryDirectory(prefix="panel_sketch_transcrypt") as tmpdir:
            root = pathlib.Path(tmpdir)
            sketch_py = root / "sketch.py"
            sketch_py.write_text(template_string.replace("{{sketch_object}}", sketch_object))

            if template_name == "pyp5js":
                arguments = [
                    "transcrypt",
                    "-xp",
                    "c:\\repos\\private\\panel-sketch\\.venv\\lib\\site-packages\\pyp5js",
                    "-k",
                    "-ks",
                    "-b",
                    "-m",
                    "-n",
                    str(sketch_py),
                ]
            else:
                arguments = ["transcrypt", "-b", "-n", "-m"] + [str(sketch_py)]
            print(" ".join(arguments))
            subprocess.run(
                arguments, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True, check=True
            )

            # We should find a way to serve the transcrypt and p5 assets locally
            sketch_js = (root / "__target__/sketch.js").read_text().replace("from './", "from '../transcrypt/")
            # results.append(sketch_js)
            return sketch_js


class PyodideCompiler(SketchCompilerBase):
    """The PyodideCompiler uses the Pyodide JS library"""

    run = param.Action(constant=True)

    sketch = param.ClassSelector(class_=SketchBase, precedence=-1, constant=True)

    _TEMPLATE_STRINGS: Dict[str, str] = PYODIDE_TEMPLATE_STRINGS

    @classmethod
    def _compile(cls, sketch_object, template_string):
        sketch_object = cls._clean_object(sketch_object)
        return template_string.replace("{{sketch_object}}", sketch_object)

    @staticmethod
    def _clean_object(value: str) -> str:
        clean = dedent(value)
        clean = clean.replace("from pyp5js import *\n", "")
        return clean


COMPILERS = {"pyodide": PyodideCompiler, "transcrypt": TranscryptCompiler}
