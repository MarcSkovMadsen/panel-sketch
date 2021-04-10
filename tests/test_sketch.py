# pylint: disable=redefined-outer-name,protected-access
# pylint: disable=missing-function-docstring,missing-module-docstring,missing-class-docstring

import panel as pn

from panel_sketch import Sketch


def test_constructor():
    Sketch()


def test_sketch_app():
    src = "https://github.com/holoviz/panel/raw/master/doc/_static/logo_stacked.png"
    image_style = "height:95%;cursor: pointer;border: 1px solid #ddd;border-radius: 4px;padding: 5px;"
    image_html = f"<img class='image-button' src='{src}' style='{image_style}'>"

    sketch = Sketch(value=image_html, height=100, width=100)
    return pn.Column(sketch, pn.Param(sketch, parameters=["clicks"]))


if __name__.startswith("bokeh"):
    # pn.extension("sketch")
    test_sketch_app().servable()
