import panel as pn

from panel_sketch import P5jsSketch


def test_constructor():
    sketch = P5jsSketch()


def test_app():
    sketch = P5jsSketch(
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

    return pn.Column(sketch.view, slider)


if __name__.startswith("bokeh"):
    test_app().servable()
