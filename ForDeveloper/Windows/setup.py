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
manifest = ''' 
<assembly xmlns="urn:schemas-microsoft-com:asm.v1" 
manifestVersion="1.0"> 
  <assemblyIdentity 
    version="0.6.8.0" 
    processorArchitecture="x86" 
    name="MyCare Card Browser" 
    type="win32" 
  /> 
  <description>MyCare Card Browser Program</description> 
  <trustInfo xmlns="urn:schemas-microsoft-com:asm.v3"> 
    <security> 
      <requestedPrivileges> 
        <requestedExecutionLevel 
          level="asInvoker" 
          uiAccess="false" 
        /> 
      </requestedPrivileges> 
    </security> 
  </trustInfo> 
  <dependency> 
    <dependentAssembly> 
      <assemblyIdentity 
        type="win32" 
        name="Microsoft.VC90.CRT" 
        version="9.0.21022.8" 
        processorArchitecture="x86" 
        publicKeyToken="1fc8b3b9a1e18e3b" 
      /> 
    </dependentAssembly> 
  </dependency> 
  <dependency> 
    <dependentAssembly> 
      <assemblyIdentity 
        type="win32" 
        name="Microsoft.Windows.Common-Controls" 
        version="6.0.0.0" 
        processorArchitecture="x86" 
        publicKeyToken="6595b64144ccf1df" 
        language="*" 
      /> 
    </dependentAssembly> 
  </dependency> 
</assembly> 
''' 

options = {"py2exe":{"compressed": 1, #压缩
                     #"optimize": 2,
                     "bundle_files": 1 #所有文件打包成一个exe文件
                     }}
setup(#service=["PyWindowsService"],
      options=options,
      zipfile=None,
      windows=[
          {
          "script": "GPA_Calc.py",
          "other_resources":[(24,1,manifest)]
          }
          ],
      )
