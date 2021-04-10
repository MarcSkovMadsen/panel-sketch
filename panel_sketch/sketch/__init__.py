from textwrap import dedent

import param

LAYOUT_NONE = (None, None, None)


class Sketch(param.Parameterized):
    html = param.String(f"""<div id="sketch-holder"></div>""")
    object = param.String()
    args = param.Dict()

    view = param.Parameter()

    @staticmethod
    def _clean_object(value: str) -> str:
        clean = dedent(value)
        clean = clean.replace("from pyp5js import *\n", "")
        return clean

    @staticmethod
    def _get_layout(value: str):
        clean = dedent(value)
        index = clean.find("createCanvas(")  # '...createCanvas(200, 200)\n\n    background(160)'
        if index == -1:
            return LAYOUT_NONE

        clean = clean[index:-1].replace("createCanvas(", "")  # '200, 200)\n\n    background(160)'
        index = clean.find(")")
        clean = clean[0:index]  # '200, 200
        args = clean.split(",")
        width = int(args[0])
        height = int(args[1])
        sizing_mode = "fixed"
        return width, height, sizing_mode
