class X :
    def __init__(self,name):
        self.__name=name

    def __test__(self):
        print (self.name)


x= X("anil")
x.__test__()