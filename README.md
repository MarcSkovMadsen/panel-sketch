![Panel Sketch Logo](https://raw.githubusercontent.com/MarcSkovMadsen/panel-sketch/main/assets/images/panel-sketch-logo.png)

# &#x270f; &#xfe0f; Panel Sketch

THIS IS APLHA SOFTWARE AND YOU MAY EXPERIENCE API CHANGES AND ROUGH EDGES.

The purpose of the `panel-sketch` package is to make it easy for Pythonistas to quickly sketch interactive visualizations and other applications running in

- The browser - also without a Python backend
- The Jupyter Notebook.
- Your favorite editor or IDE.

It is heavily inspired by [p5js](https://p5js.org/get-started/), [p5js sketches](https://editor.p5js.org/p5/sketches) and [pyp5js](https://github.com/berinhard/pyp5js) &#10084;&#65039; It is not limited to the p5js universe though.

You can also think of it as a [Code Sandbox](https://codesandbox.io/) or [JS Fiddle](https://jsfiddle.net/) but for #Python, #PyData and #PyViz &#128013;.

[![Panel Sketch Reference Example](https://github.com/MarcSkovMadsen/panel-sketch/blob/main/assets/images/panel-sketch-binder.gif?raw=true)](https://mybinder.org/v2/gh/marcskovmadsen/panel-sketch/HEAD?urlpath=lab/tree/examples/Sketch.ipynb)

It leverages the powerful `Python` to `Javascript` frameworks [Pyodide](https://github.com/pyodide/pyodide) and [Transcrypt](https://www.transcrypt.org/) &#128170;. Potentially [Brython](https://brython.info/) and other could be added in the future.

Check out the `panel-sketch` examples on **Binder**

| Jupyter Notebook | Jupyter Labs | Panel Apps |
| - | - | - |
| [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/marcskovmadsen/panel-sketch/HEAD?filepath=examples) | [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/marcskovmadsen/panel-sketch/HEAD?urlpath=lab/tree/examples) | [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/marcskovmadsen/panel-sketch/HEAD?urlpath=panel) |

## License

The `panel-sketch` python package and repository is open source and free to use (MIT License).

## Installation

With `pip`

```bash
pip install panel-sketch
```

## Usage

```python
from panel_sketch import Sketch

import panel as pn
pn.config.sizing_mode="stretch_width"

args={"r": 10, "g": 200, "b": 40} # This will give us the color for our sketch

sketch_python = """
# https://p5js.org/examples/interaction-wavemaker.html


from pyp5js import *

t = 0


def setup():
    createCanvas(600, 600)
    stroke(250)
    strokeWeight(3)
    fill(window.args.r, window.args.g, window.args.b)


def draw():
    global t
    background(10, 10)
    fill(window.args.r, window.args.g, window.args.b)

    xAngle = map(mouseX, 0, width, -4 * PI, 4 * PI, True)
    yAngle = map(mouseY, 0, height, -4 * PI, 4 * PI, True)
    for x in range(0, width, 30):
        for y in range(0, height, 30):

            angle = xAngle * (x / width) + yAngle * (y / height)

            myX = x + 20 * cos(2 * PI * t + angle)
            myY = y + 20 * sin(2 * TWO_PI * t + angle)

            ellipse(myX, myY, 10)

    t = t + 0.01
"""

sketch = Sketch(object=sketch_python, template="pyp5js", compiler="pyodide", args=args)
sketch.viewer.view.servable()
```

![Basic Example](https://github.com/MarcSkovMadsen/panel-sketch/blob/main/assets/images/panel-sketch-basic-example.png?raw=true)

## Reference Guides

### [Sketch Reference Example](https://github.com/MarcSkovMadsen/panel-sketch/blob/main/examples/Sketch.ipynb)

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/marcskovmadsen/panel-sketch/HEAD?urlpath=lab/tree/examples/Sketch.ipynb)

## Examples

### [Gallery App](https://github.com/MarcSkovMadsen/panel-sketch/blob/main/examples/pyp5js/gallery/gallery.py)

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/marcskovmadsen/panel-sketch/HEAD?urlpath=lab/tree/examples/pyp5js/gallery/gallery.py)

## Additional Resources

You can find more inspiration via the links below.

- [p5js](https://p5js.org/get-started/) and [p5js sketches](https://editor.p5js.org/p5/sketches)
- [pyp5js](https://github.com/berinhard/pyp5js)
- [Pyodide](https://github.com/pyodide/pyodide)
- [Transcrypt](https://www.transcrypt.org/)
- [Brython](https://brython.info/)
- [Panel](https://panel.holoviz.org)
- [Awesome Panel](https://awesome-panel.org)

## Roadmap

When I get the time I would like to

- add example using basic template to Sketch Reference Example
- Add `basic` template examples.
- Enable using the content of notebook cells instead of a string to instantite `Sketch`.
- Add more notebook examples
- Enable easy import and export of sketches
- Find out how I can serve the target js modules in notebook (Enable Transcrypt in Notebook).
- Support [alternatives](https://www.slant.co/options/147/alternatives/~p5-js-alternatives) to p5js like [three.js](https://threejs.org/)
- change `window.args` to `args` reference.
- change `Sketch.viewer.view` to `Sketch.viewer`. Similarly for `Sketch.editor`.
- (re-)align with pyp5js
- Add example app to [Awesome Panel](https://awesome-panel.org).
- Support extensions to p5js like [m5.js](https://ml5js.org/)
- Create youtube tutorial video
- Add badges for 100% test coverage etc.
- Distribute as conda package

## Change Log

- 20210410: First Release to PyPi.