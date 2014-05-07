import datetime
import os
from sys import version as sysversion
import other

version = 1.0
print(version)
print(sysversion)

print(datetime.datetime.now())
#other.method()
other.something = "boo!"
print( dir(other.method)  )
print(type(other.method))