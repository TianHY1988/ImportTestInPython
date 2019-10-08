'''
    this is the main function to test 
    the Absolute vs Relative Imports in Python

    there are five absolute imports below
'''

# absolute imports
from package1 import module1
from package1.module2 import function1
from package2 import class1 #importing package2 essentially imports the package2’s __init__.py file as a module
from package2.subpackage2.module5 import function2 as f2
from package1.subpackage1 import module6
import package2.module4

# use two funtions imported above
function1()
f2() #use f2 instead of function2, there will be an error if function2 is used 