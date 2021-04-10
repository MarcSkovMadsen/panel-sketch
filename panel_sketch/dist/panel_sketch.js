/*!
 * Copyright (c) 2012 - 2021, Anaconda, Inc., and Bokeh Contributors
 * All rights reserved.
 * 
 * Redistribution and use in source and binary forms, with or without modification,
 * are permitted provided that the following conditions are met:
 * 
 * Redistributions of source code must retain the above copyright notice,
 * this list of conditions and the following disclaimer.
 * 
 * Redistributions in binary form must reproduce the above copyright notice,
 * this list of conditions and the following disclaimer in the documentation
 * and/or other materials provided with the distribution.
 * 
 * Neither the name of Anaconda nor the names of any contributors
 * may be used to endorse or promote products derived from this software
 * without specific prior written permission.
 * 
 * THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
 * AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
 * IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
 * ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE
 * LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
 * CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
 * SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
 * INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
 * CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
 * ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF
 * THE POSSIBILITY OF SUCH DAMAGE.
 */
(function(root, factory) {
  factory(root["Bokeh"], undefined);
})(this, function(Bokeh, version) {
  var define;
  return (function(modules, entry, aliases, externals) {
    const bokeh = typeof Bokeh !== "undefined" && (version != null ? Bokeh[version] : Bokeh);
    if (bokeh != null) {
      return bokeh.register_plugin(modules, entry, aliases);
    } else {
      throw new Error("Cannot find Bokeh " + version + ". You have to load it prior to loading plugins.");
    }
  })
({
"a6a4fae5e8": /* index.js */ function _(require, module, exports, __esModule, __esExport) {
    __esModule();
    const tslib_1 = require("tslib");
    const SketchExtensions = tslib_1.__importStar(require("8fbb31f6e4") /* ./models/ */);
    exports.SketchExtensions = SketchExtensions;
    const base_1 = require("@bokehjs/base");
    base_1.register_models(SketchExtensions);
},
"8fbb31f6e4": /* models\index.js */ function _(require, module, exports, __esModule, __esExport) {
    __esModule();
    var sketch_1 = require("b09786f089") /* ./sketch */;
    __esExport("Sketch", sketch_1.Sketch);
},
"b09786f089": /* models\sketch.js */ function _(require, module, exports, __esModule, __esExport) {
    __esModule();
    // See https://docs.bokeh.org/en/latest/docs/reference/models/layouts.html
    const html_box_1 = require("@bokehjs/models/layouts/html_box");
    // The view of the Bokeh extension/ HTML element
    // Here you can define how to render the model as well as react to model changes or View events.
    class SketchView extends html_box_1.HTMLBoxView {
        connect_signals() {
            super.connect_signals();
            this.connect(this.model.properties.value.change, () => {
                this.render();
            });
        }
        render() {
            console.log("render");
            console.log(this.model);
            super.render();
            this.el.innerHTML = this.model.value;
            this.valueElement = this.el.firstElementChild;
            this.valueElement.addEventListener("click", () => { this.model.clicks += 1; }, false);
        }
    }
    exports.SketchView = SketchView;
    SketchView.__name__ = "SketchView";
    // The Bokeh .ts model corresponding to the Bokeh .py model
    class Sketch extends html_box_1.HTMLBox {
        constructor(attrs) {
            super(attrs);
        }
        static init_Sketch() {
            this.prototype.default_view = SketchView;
            this.define(({ String, Int }) => ({
                value: [String, "<button style='width:100%'>Click Me</button>"],
                clicks: [Int, 0],
            }));
        }
    }
    exports.Sketch = Sketch;
    Sketch.__name__ = "Sketch";
    Sketch.__module__ = "panel_sketch.models.sketch";
    Sketch.init_Sketch();
},
}, "a6a4fae5e8", {"index":"a6a4fae5e8","models/index":"8fbb31f6e4","models/sketch":"b09786f089"}, {});});
//# sourceMappingURL=panel_sketch.js.map
