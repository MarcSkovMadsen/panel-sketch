"""Sketch Bokeh Model"""
from bokeh.core.properties import Int, String
from bokeh.models import HTMLBox

DEFAULT_OBJECT = "<button style='width:100%'>Click Me</button>"


class Sketch(HTMLBox):
    """Example implementation of a Custom Bokeh Model"""

    value = String(default=DEFAULT_OBJECT)
    clicks = Int(default=0)
