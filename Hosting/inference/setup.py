# ai_model_hosting/cpp_inference/setup.py
from setuptools import setup, Extension
from pybind11.setup_helpers import Pybind11Extension, build_ext

ext_modules = [
    Pybind11Extension("inference", ["inference.cpp"]),
]

setup(
    name="inference",
    ext_modules=ext_modules,
    cmdclass={"build_ext": build_ext},
)
