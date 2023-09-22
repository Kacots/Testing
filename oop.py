class Name:
    def __init__(self,name):
        self.__name = name
    
    def getName(self):
        return self.__name

    def setName(self,name):
        self.__name = name
        return self.__name

class ID:
    def __init__(self,id):
        self.__id = id

    def getId(self):
        return self.__id

    def setId(self,new_id):
        self.__id = new_id
        return self__id

name = Name("panca")
id = ID(17639729)
print(name.getName())
print(id.getId())








