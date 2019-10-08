def function2():
    print("~~~")
    print("I'm function2 in module5 imported by main through absolute import")
    #print("the package of module5 : "+(__package__ or "no package"))
    #print("the file of module5: "+ __file__)

def function4():
    print("~~~")
    print("I'm function4 in module5 imported by module3 through relative import")
    #print("the package of module5 : "+(__package__ or "no package"))
    #print("the file of module5: "+ __file__)