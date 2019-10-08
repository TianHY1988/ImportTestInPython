class class1():
    print("~~~")
    print("I'm class1 in __init__ of subpackage2"+
    "imported by main through absolute import")
    #print("the package of package2 : "+(__package__ or "no package"))
    #print("the file of package2: "+ __file__)

class class2():
    print("~~~")
    print("I'm class2 in __init__ of subpackage2"+
    "imported by module3 through relative import")