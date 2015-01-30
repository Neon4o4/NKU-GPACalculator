# mysetup.py
from distutils.core import setup
import py2exe

#==========================
#bundle_files:
#3 (默认)不打包
#2 打包，但不打包Python解释器
#1 打包，包括Python解释器
#==========================
#
#
options = {"py2exe":{"compressed": 1, #压缩
                     "optimize": 2,
                     "bundle_files": 1 #所有文件打包成一个exe文件
                     }}
setup(#service=["PyWindowsService"],
      options=options,
      zipfile=None,
      windows=[
          {
          "script": "GPA_Calc.py"
          }
          ],
      )
