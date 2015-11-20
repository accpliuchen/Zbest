
class MENU:

    def __init__(self,id,name,price,description,path):
        self.__id = id
        self.__name=name
        self.__price=price
        self.__description=description
        self.__path=path

    def getId(self):
        return self.__id

    def setId(self, id):
        self.__id = id
    
    
    def getName(self):
        return self.__name

    def setName(self, name):
        self.__name = name
        
    def getPrice(self):
        return self.__price

    def setPrice(self, price):
        self.__price = price
        
    def getDescription(self):
        return self.__description

    def setDescription(self, description):
        self.__description = description
        
    def getPath(self):
        return self.__path

    def setPath(self, path):
        self.__path = path
   