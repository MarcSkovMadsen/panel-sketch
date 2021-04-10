// See https://docs.bokeh.org/en/latest/docs/reference/models/layouts.html
import { HTMLBox, HTMLBoxView } from "@bokehjs/models/layouts/html_box"

// See https://docs.bokeh.org/en/latest/docs/reference/core/properties.html
import * as p from "@bokehjs/core/properties"

// The view of the Bokeh extension/ HTML element
// Here you can define how to render the model as well as react to model changes or View events.
export class SketchView extends HTMLBoxView {
    model: Sketch
    valueElement: any // Element

    connect_signals(): void {
        super.connect_signals()

        this.connect(this.model.properties.value.change, () => {
            this.render();
        })
    }

    render(): void {
        console.log("render")
        console.log(this.model)
        super.render()
        this.el.innerHTML = this.model.value
        this.valueElement = this.el.firstElementChild

        this.valueElement.addEventListener("click", () => {this.model.clicks+=1;}, false)
    }
}

export namespace Sketch {
    export type Attrs = p.AttrsOf<Props>
    export type Props = HTMLBox.Props & {
        value: p.Property<string>,
        clicks: p.Property<number>,
    }
}

export interface Sketch extends Sketch.Attrs { }

// The Bokeh .ts model corresponding to the Bokeh .py model
export class Sketch extends HTMLBox {
    properties: Sketch.Props

    constructor(attrs?: Partial<Sketch.Attrs>) {
        super(attrs)
    }

    static __module__ = "panel_sketch.models.sketch"

    static init_Sketch(): void {
        this.prototype.default_view = SketchView;

        this.define<Sketch.Props>(({String, Int}) => ({
            value: [String, "<button style='width:100%'>Click Me</button>"],
            clicks: [Int, 0],
        }))
    }
}