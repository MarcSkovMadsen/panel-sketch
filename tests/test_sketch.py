# pylint: disable=redefined-outer-name,protected-access
# pylint: disable=missing-function-docstring,missing-module-docstring,missing-class-docstring
import panel as pn

from panel_sketch import Sketch


def test_constructor():
    Sketch()


def test_app():
    sketch = Sketch(
        # Test that it also works indented
        object="""
    def setup():

        createCanvas(200, 200)

        background(160)

    def draw():

        fill("blue")

        background(200)

        radius = sin(frameCount / 60) * window.args.value + 50

        ellipse(100, 100, radius, radius)
    """,
    )

    slider = pn.widgets.FloatSlider(value=50, start=10, end=100, step=1)

    @pn.depends(value=slider, watch=True)
    def _update_value(value):
        sketch.args = dict(value=value)

    _update_value(slider.value)

    return pn.Column(sketch.viewer, slider)


if __name__.startswith("bokeh"):
    test_app().servable()
