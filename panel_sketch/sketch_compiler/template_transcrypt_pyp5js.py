from pyp5js import *

{{sketch_object}}

event_functions = {}
try:
    event_functions["deviceMoved"]= deviceMoved
except:
    pass
try:
    event_functions["deviceTurned"]= deviceTurned
except:
    pass
try:
    event_functions["deviceShaken"]= deviceShaken
except:
    pass
try:
    event_functions["keyPressed"]= keyPressed
except:
    pass
try:
    event_functions["keyReleased"]= keyReleased
except:
    pass
try:
    event_functions["keyTyped"]= keyTyped
except:
    pass
try:
    event_functions["mouseMoved"]= mouseMoved
except:
    pass
try:
    event_functions["mouseDragged"]= mouseDragged
except:
    pass
try:
    event_functions["mousePressed"]= mousePressed
except:
    pass
try:
    event_functions["mouseReleased"]= mouseReleased
except:
    pass
try:
    event_functions["mouseClicked"]= mouseClicked
except:
    pass
try:
    event_functions["doubleClicked"]= doubleClicked
except:
    pass
try:
    event_functions["mouseWheel"]= mouseWheel
except:
    pass
try:
    event_functions["touchStarted"]= touchStarted
except:
    pass
try:
    event_functions["touchMoved"]= touchMoved
except:
    pass
try:
    event_functions["touchEnded"]= touchEnded
except:
    pass
try:
    event_functions["windowResized"]= windowResized
except:
    pass


def start_p5(setup_func, draw_func, event_functions):
    """
    This is the entrypoint function. It accepts 2 parameters:
    - setup_func: a Python setup callable
    - draw_func: a Python draw callable
    - event_functions: a config dict for the event functions in the format:
                       {"eventFunctionName": python_event_function}
    This method gets the p5js's sketch instance and injects them
    """
    # Hack: For some reason it is needed
    sketchElement.innerText=""

    def sketch_setup(p5_sketch):
        p5_sketch.setup = global_p5_injection(p5_sketch)(setup_func)
        p5_sketch.draw = global_p5_injection(p5_sketch)(draw_func)


    instance = __new__(p5(sketch_setup, 'sketch-element'))

    # inject event functions into p5
    event_function_names = (
        "deviceMoved", "deviceTurned", "deviceShaken", "windowResized",
        "keyPressed", "keyReleased", "keyTyped",
        "mousePressed", "mouseReleased", "mouseClicked", "doubleClicked",
        "mouseMoved", "mouseDragged", "mouseWheel",
        "touchStarted", "touchMoved", "touchEnded"
    )

    for f_name in [f for f in event_function_names if event_functions.get(f, None)]:
        func = event_functions[f_name]
        event_func = global_p5_injection(instance)(func)
        setattr(instance, f_name, event_func)

start_p5(setup, draw, event_functions)