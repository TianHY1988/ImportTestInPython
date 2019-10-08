'''

'''
# Relative Imports
from .module2 import function3

print("~~~")
print("I'm module1 in package1 imported by main through absolute import")
#print("the package of module1 : "+(__package__ or "no package"))
#print("the file of module1: "+ __file__)

print("~~~")
print("run function3 imported from module2")
function3()