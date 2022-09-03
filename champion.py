class Champion:
    name : str
    length : int  

    def __init__(self,name) -> None:
        self.__name = name
        self.__length = len(name)

    @property
    def name(self) -> str:
        return self.__name

    @property
    def length(self) -> int:
        return self.__length

    @name.setter
    def name(self,new_name):
        self.__name = new_name
    
    @length.setter
    def length(self,new_length):
        self.__length = new_length


    """Delete part will be handle after -- TODO --  """
    @name.deleter
    def name(self):
        print("Deleted the name of"+self.name)
        del self.__name

    @length.deleter
    def length(self):
        print("Deleted the length of"+self.length)
        del self.__length