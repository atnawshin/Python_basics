#xxargs - works like dictionary
#multiple value pass korar jonno ** use korte hobe

def student(**details):
    print(details["name"])

student(id=101,name="Joye")