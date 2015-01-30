# mysetup.py
from distutils.core import setup
import glob
import py2exe
import os

setup(windows=[{"script":os.path.split(os.path.realpath(__file__))[0]+"/GPA_Calc.py"}])