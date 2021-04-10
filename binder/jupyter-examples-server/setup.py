"""This setup.py will install a package that configures the jupyter-server-proxy to
panel serve the example notebooks."""
import setuptools

setuptools.setup(
    name="jupyter-panel-examples-server",
    py_modules=["__init__"],
    entry_points={
        "jupyter_serverproxy_servers": [
            "panel = __init__:panel_serve_examples",
        ]
    },
    install_requires=["jupyter-server-proxy"],
)
