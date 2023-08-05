from setuptools import setup, find_packages
import codecs
import os

VERSION = '1.0.2'
DESCRIPTION = 'MicroPythonPy'
LONG_DESCRIPTION = 'A package for MACHINE LEARNING and using with micro python'

# Setting up
setup(
    name="MicroMachinePy",
    version=VERSION,
    author="HarshPro",
    author_email="patidarharsh16122008@gmail.com",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=[],
    keywords=['MACHINE LEARNING', "ESP32", "RASPBERRY PI", "ARDUINO", "MicroMachinePy"],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)
