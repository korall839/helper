from setuptools import setup, find_packages

setup(
    name="helper", 
    version="1.0.0",
    packages=find_packages(),
    py_modules=["helper"],
    install_requires=[
        "windows-curses; platform_system=='Windows'", 
    ],
)