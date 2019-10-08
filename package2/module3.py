# Relative Imports
from . import class2
from .subpackage2.module5 import function4

print("~~~")
print("I'm module3 in package2 imported by module4 through absolut import")
#print("the package of package2 : "+(__package__ or "no package"))
#print("the file of package2: "+ __file__)

function4()