"""The SketchEditor enables editing the SketchBase and derived classes"""
import datetime

import panel as pn
import param

from .sketch_base import SketchBase

EDITOR_HEIGHT = 600
EDITOR_MARGIN = (20, 5, 10, 5)
MAX_LOG_LINES = 50


class SketchEditor(param.Parameterized):
    """The SketchEditor enables editing the SketchBase and derived classes"""

    compile = param.Action()

    view = param.Parameter()

    sketch = param.ClassSelector(class_=SketchBase, constant=True, precedence=-1)

    def __init__(self, **params):
        super().__init__(**params)

        self.compile = self._compile_sketch
        self._create_view()

    def _create_view(self):
        sketch: SketchBase = self.sketch
        build_button = pn.widgets.Button(
            name="▶", button_type="primary", margin=(10, 0, 10, 5), width=50, sizing_mode="fixed"
        )

        self._python_editor = pn.widgets.Ace(
            name="🐍 PYTHON",
            language="python",
            height=EDITOR_HEIGHT,
            value=sketch.object,
            margin=EDITOR_MARGIN,
        )

        # # pylint: disable=no-value-for-parameter,no-member
        @param.depends(code=sketch.param.object, watch=True)
        def _update_python_editor(code):
            self._python_editor.value = code

        self._html_editor = pn.widgets.Ace(
            name="🗎 HTML",
            language="html",
            height=EDITOR_HEIGHT,
            value=sketch.html,
            margin=EDITOR_MARGIN,
        )

        @param.depends(code=sketch.param.html, watch=True)
        def _update_html_editor(code):
            self._html_editor.value = code

        self._css_editor = pn.widgets.Ace(
            name="🎨 CSS",
            language="css",
            height=EDITOR_HEIGHT,
            value=sketch.css,
            margin=EDITOR_MARGIN,
        )

        @param.depends(code=sketch.param.css, watch=True)
        def _update_css_editor(code):
            self._css_editor.value = code

        self._javascript_editor = pn.widgets.Ace(
            name="☕ JS",
            language="javascript",
            readonly=True,
            height=EDITOR_HEIGHT,
            value=sketch.javascript,
            margin=EDITOR_MARGIN,
        )

        @param.depends(code=sketch.param.javascript, watch=True)
        def _update_javascript_editor(code):
            self._javascript_editor.value = code

        self._log = pn.widgets.TextAreaInput(
            name="⚠️ Log", height=EDITOR_HEIGHT, margin=EDITOR_MARGIN, disabled=True
        )

        build_button.on_click(self.compile)

        self.view = pn.Column(
            pn.Row(build_button),
            pn.Tabs(
                self._python_editor,
                self._html_editor,
                self._css_editor,
                self._javascript_editor,
                self._log,
            ),
        )

    def _compile_sketch(self, _=None):
        sketch = self.sketch
        sketch.html = self._html_editor.value
        sketch.css = self._css_editor.value
        if sketch.object == self._python_editor.value:
            # Hack to force update
            sketch.object = self._python_editor.value + "\n"
        else:
            sketch.object = self._python_editor.value

        log_value = "\n".join(self._log.value.split("\n")[:MAX_LOG_LINES])
        self._log.value = (
            datetime.datetime.now().strftime("%H:%M:%S:  ") + "Build" + "\n" + log_value
        )
