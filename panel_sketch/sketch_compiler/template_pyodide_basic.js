console.log("pyodide basic")
let userCode = `
{{sketch_object}}
`;

function runCode() {
    let code = userCode

    if (window.instance) {
      window.instance.canvas.remove();
    }

    console.log("Python execution output:");
    pyodide.runPython(code);
}

languagePluginLoader.then(() => {
    pyodide.runPython(`
      import io, code, sys
      from js import pyodide, window, document
      print(sys.version)
    `)

    window.runSketchCode = (code) => {
      userCode = code;
      runCode();
    }

    runCode();
});