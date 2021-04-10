"""The Sketch Model"""
import param
from panel.widgets.base import Widget

from .models import sketch

class Sketch(Widget):
    """The Sketch Model provides ..."""
    # Set the Bokeh model to use
    _widget_type = sketch.Sketch

    # Rename Panel Parameters -> Bokeh Model properties
    # Parameters like title that does not exist on the Bokeh model should be renamed to None
    _rename = {
        "title": None,
    }

    # Parameters to be mapped to Bokeh model properties
    value = param.String(default=sketch.DEFAULT_OBJECT)
    clicks = param.Integer(default=0)
