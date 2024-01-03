from setuptools import setup

setup(
    name="met-fetch",
    version="0.1.0",
    py_modules=["met-fetch"],
    entry_points={
        "console_scripts": [
            "met-fetch = fetch:main",
        ],
    },
)
