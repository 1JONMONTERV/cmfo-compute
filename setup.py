from setuptools import setup, find_packages

setup(
    name="cmfo_compute",
    version="1.0.0",
    packages=find_packages(),
    install_requires=[
        "numpy",
    ],
    author="CMFO Research",
    description="Fractal Computing Library based on CMFO T7-phi automaton.",
)
