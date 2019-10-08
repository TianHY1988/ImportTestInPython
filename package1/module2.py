'''
    
'''
print("I'm module2 and imported only one time")
def function1():
    print("~~~")
    print("I'm function1 in module2 imported by main through absolute import")
    #print("the package of module2 : "+(__package__ or "no package"))
    #print("the file of module2: "+ __file__)

def function3():
    print("~~~")
    print("I'm function3 in module2 imported by module1 through relative import")