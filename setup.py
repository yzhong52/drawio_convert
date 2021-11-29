from setuptools import setup

setup(
    name="drawio_convert",
    version="0.1",
    description="A script for export all drawio files under this folder to images (i.e. png).",
    url="https://github.com/yzhong52/drawio_convert",
    author="Yuchen Z.",
    license="MIT",
    packages=["drawio_convert"],
    zip_safe=False,
    entry_points={
        "console_scripts": ["drawio=drawio_convert.drawio_convert:convert"],
    },
)
