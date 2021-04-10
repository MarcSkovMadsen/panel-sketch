"""Configures Panel.extension"""
from panel import extension

# Enables using pn.extension("sketch", ...)
# pylint: disable=protected-access
extension._imports["sketch"] = "panel_sketch.models.sketch"
# pylint: enable=protected-access
